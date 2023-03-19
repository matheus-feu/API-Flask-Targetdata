from dataclasses import dataclass


@dataclass
class LoggerConfigElasticsearch:
    host: str = 'localhost:9200'
    index_name: str = 'logs_api'
