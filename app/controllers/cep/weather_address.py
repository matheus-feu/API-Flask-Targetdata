import requests
import xmltodict
from flask import request, jsonify
from flask_jwt_extended import jwt_required
from unidecode import unidecode
import xml.etree.ElementTree as ET


from app import app, require_keys
from app.config import APICep, APIInpe
from app.decorators.auth import token_required
from app.decorators.regex_cep_validate import regex_cep_validate


@app.route('/weather-address', methods=['GET'])
@require_keys(['cep'])
@regex_cep_validate
@token_required()

def address_weather(current_user):

    # Faz a consulta do endereço pelo CEP
    cep = request.json['cep']

    via_cep_response = requests.get(f"{APICep.URL}{cep}/json/")

    via_cep_data_json = via_cep_response.json()

    # Obtém a cidade retornada pelo ViaCEP
    city = via_cep_data_json.get('localidade')

    if not city:
        return {'message': 'Cidade não encontrada'}, 404

    # Formata a cidade para consulta no INPE
    city_formated = unidecode(city)

    # Faz a consulta da cidade na API do INPE e obter o código da cidade
    city_code = generate_cod_inpe(city_formated, city)

    if city_code is not None:
        request_inpe = requests.get(f'{APIInpe.URL_PREVISAO}{city_code}/previsao.xml')
        response_inpe_xml = request_inpe.content
        response_inpe_dict = xmltodict.parse(response_inpe_xml)
        response_inpe_dict.update({"cep": via_cep_data_json})

        return response_inpe_dict

    return {'error': f'Clima de 4 dias na cidade {city} não encontrada'}


def generate_cod_inpe(city_formated, city):
    response = requests.get(
        APIInpe.URL,
        params={'city': city_formated})

    response_xml = ET.fromstring(response.content)
    codigo = None
    for cidade in response_xml.findall('cidade'):
        if cidade.findtext('nome') == city:
            codigo = cidade.findtext('id')
            break

    if codigo:
        return codigo
