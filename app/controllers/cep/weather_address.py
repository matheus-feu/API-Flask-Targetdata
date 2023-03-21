import xml.etree.ElementTree as ET

import requests
import xmltodict
from flasgger import swag_from
from flask import request
from unidecode import unidecode

from app import es_logger, app
from app.config.urls_api import APICep, APIInpe
from app.decorators.auth import token_required
from app.decorators.regex_cep_validate import regex_cep_validate
from app.decorators.required_keys import require_keys
from app.utils.http_request_info import HttpRequestInfo

http_request_info = HttpRequestInfo()
ip_address = http_request_info.get_request_info('ip_address')
user_agent = http_request_info.get_request_info('user_agent')
geo_location = http_request_info.get_request_info('geo_location', ip_address)
city_ip = geo_location['city'] if geo_location['city'] else 'Unknown'
provider = geo_location['org'] if geo_location['org'] else 'Unknown'

log_format = f'IP: {ip_address} - User-Agent: {user_agent} - Provider: {provider} - City: {city_ip}'


@app.route('/api/weather-address', methods=['POST'])
@token_required()
@require_keys(['cep'])
@regex_cep_validate
@swag_from('../../docs/cep.yml')
def address_weather(current_user):
    """Esta função faz a consulta do endereço pelo CEP na API ViaCep
    e retorna a previsão do tempo em 4 dias"""

    cep = request.json['cep']

    # Faz a consulta do endereço pelo CEP na API ViaCep
    via_cep_response = requests.get(f"{APICep.URL}{cep}/json/")

    via_cep_data_json = via_cep_response.json()

    # Obtém a cidade retornada pelo ViaCEP
    city = via_cep_data_json.get('localidade')

    if not city:
        return {'message': f'Cidade não encontrada: {city}'}, 404

    # Formata a cidade para consulta no INPE
    city_formated = unidecode(city)

    # Faz a consulta da cidade na API do INPE e obter o código da cidade
    city_code = generate_cod_inpe(city_formated, city)

    if city_code is not None:
        request_inpe = requests.get(f'{APIInpe.URL_PREVISAO}{city_code}/previsao.xml')
        response_inpe_xml = request_inpe.content
        response_inpe_dict = xmltodict.parse(response_inpe_xml)
        response_inpe_dict.update({"cep": via_cep_data_json})
        es_logger.info(f'Consulta sucedida: {cep} - {log_format} - Codígo: {city_code}')

        return response_inpe_dict
    es_logger.warning(f'Não foi encontrado o clima para 4 dias na cidade {city} na API do INPE.')
    return {'error': f'Não foi encontrado o clima para 4 dias na cidade {city} na API do INPE.'}, 404


def generate_cod_inpe(city_formated, city):
    """Esta função faz a consulta da cidade na API do INPE e obtém o
    código da cidade e retorna"""

    response = requests.get(
        APIInpe.URL, params={'city': city_formated})

    response_xml = ET.fromstring(response.content)
    codigo = None
    for cidade in response_xml.findall('cidade'):
        if cidade.findtext('nome') == city:
            codigo = cidade.findtext('id')
            break

    if codigo:
        return codigo
