from dataclasses import dataclass


@dataclass
class LoggerConfigElasticsearch:
    """Configurações do Elasticsearch para a coleta de logs.
    Definindo o host para gravar os logs."""

    host: str = 'localhost:9200'
    index_name: str = 'logs_api'
