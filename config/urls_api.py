class APIInpe:
    """Configuração de URLs de APIs externas."""
    URL = 'http://servicos.cptec.inpe.br/XML/listaCidades'
    URL_PREVISAO = 'http://servicos.cptec.inpe.br/XML/cidade/'


class APICep:
    """Configuração de URLs de APIs externas."""
    URL = 'https://viacep.com.br/ws/'


class APIRequestInspectionBin:
    """Configuração de URLs de APIs externas."""
    URL = 'http://httpbin.org/'


class APIGeoLocation:
    """Configuração de URLs de APIs externas."""
    URL = 'http://ip-api.com/json/'


class ElasticsearchLogs:
    URL = 'http://localhost:9200/logs_api/_search'