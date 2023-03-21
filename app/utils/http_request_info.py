import requests as req
from app.config.urls_api import APIRequestInspectionBin, APIGeoLocation



class HttpRequestInfo:

    def get_request_info(self, type_request, ip_address=None):
        """
        Esta função tem um dicionário (dispatch table) com as informações de
        requisição e retorna o valor da requisição
        """

        http_requests_dict = {
            'user_agent': {
                'url': f"{APIRequestInspectionBin.URL}user-agent",
                'key': 'user-agent',
                'message': 'User-agent not found'
            },
            'ip_address': {
                'url': f"{APIRequestInspectionBin.URL}ip",
                'key': 'origin',
                'message': 'Ip address not found'
            },
            'geo_location': {
                'url': f"{APIGeoLocation.URL}{ip_address}",
                'key': 'status',
                'message': 'Geo location not found'
            }
        }

        # Desempacota o dicionário
        url, key, message = http_requests_dict[type_request].values()

        # Faz a requisição e retorna o valor da requisição
        response_value_http = message
        response_http = req.get(url)
        response_http_json = response_http.json()

        # Se a requisição for de localização geográfica, retorna o json
        if response_http_json.get(key):
            if type_request == 'geo_location':
                response_value_http = response_http_json
            else:
                response_value_http = response_http_json.get(key)
        return response_value_http
