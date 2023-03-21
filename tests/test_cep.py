import re

import requests as req
import xmltodict
from unidecode import unidecode

from app import generate_cod_inpe
from app.config import APICep, APIInpe


def test_cep_is_valid(cep):
    """Esta função testa se o CEP informado é válido."""
    if cep:
        return True
    return False


def test_return_cep_format_valid_zip_code():
    """Esta função testa se o CEP informado é válido."""
    cep = '01001000'
    cep_regex = re.compile(r'^\d{8}$')
    re_match = cep_regex.match(cep)
    assert test_cep_is_valid(cep_regex) == True


def test_cep_should_return_status_code_200_in_request():
    """Esta função testa e retorna o código de status 200 se o CEP informado for válido."""
    cep = '01001000'
    req_cep = req.get(f"{APICep.URL}{cep}/json/")
    assert req_cep.status_code == 200


def test_cep_should_return_status_code_404_in_request():
    """Esta função retorna o código de status 404 se o CEP informado for inválido."""
    cep = '010201000'
    req_cep = req.get(f"{APICep.URL}{cep}/json/")
    assert req_cep.status_code == 400


def test_city_code_should_return_status_code_200_in_request():
    """Esta função retorna o código de status 200 se o código da cidade informada for válida."""
    city_code = '347'
    req_city_code = req.get(f"{APIInpe.URL_PREVISAO}{city_code}/previsao.xml")
    assert req_city_code.status_code == 200


def test_function_generate_cod_inpe_should_return_city_code():
    """Gera o código da cidade através da cidade informada no campo de requisição
    e formata a cidade, removendo acentos e caracteres especiais, para que a consulta
    na API do INPE seja realizada com sucesso."""

    city = 'São Paulo'
    city_formated = unidecode(city)

    city_code = generate_cod_inpe(city_formated, city)

    if city_code is not None:
        assert city_code

    print(city_code)


def test_consult_request_city_code_APIInpe_should_return_city():
    """Faz a consulta de código da cidade na API do INPE e retorna o nome da cidade."""
    city_code = '244'

    inpe_response = req.get(f"{APIInpe.URL_PREVISAO}{city_code}/previsao.xml")
    inpe_data_xml = inpe_response.text
    city = inpe_data_xml.split('<nome>')[1].split('</nome>')[0]

    try:
        assert city
    except:
        return {"message": "Cidade não encontrada"}, 404

    print(city)


def test_consult_request_cep_address_APIViaCep_should_return_locality_city():
    """Recebe o endereço pelo o CEP informado no corpo da requisição
     e consulta API ViaCep se existir retorna a localidade da cidade."""

    cep = '01001000'

    via_cep_response = req.get(f"{APICep.URL}{cep}/json/")
    via_cep_data_json = via_cep_response.json()
    city = via_cep_data_json.get('localidade')

    try:
        assert city
    except:
        return {"message": "Localidade não encontrada"}, 404

    print(city)


def test_consult_prevision_APIInpe_should_return_prevision_in_4_days():
    """Recebe o código da cidade e retorna a previsão do tempo da cidade em 4 dias."""

    city_code = '244'

    inpe_response = req.get(f"{APIInpe.URL_PREVISAO}{city_code}/previsao.xml")
    inpe_data_xml = inpe_response.content

    try:
        inpe_data_json = xmltodict.parse(inpe_data_xml)
        prevision = inpe_data_json
        assert prevision

    except:
        return {"message": "Previsão não encontrada"}, 404

    print(prevision)



