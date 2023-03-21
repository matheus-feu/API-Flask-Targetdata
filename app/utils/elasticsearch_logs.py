import logging

from elasticsearch import Elasticsearch


class ElasticSearchLogger(logging.Logger):
    """
    Essa classe é responsável por criar um logger que envia os logs para o Elasticsearch,
    salva os logs no ES com o formato do documento. Há metodos para cada tipo de log, retornando a
    mensagem de log.
    """

    def __init__(self, index_name, elasticsearch_host):
        super().__init__(index_name)
        self.es = Elasticsearch([elasticsearch_host])
        self.setLevel(logging.INFO)
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.addHandler(handler)
        self.index_name = index_name

    def log(self, level, message):
        document = {
            'level': level,
            'message': message,
            'logger': self.index_name
        }
        self.es.index(index=self.index_name, body=document)

    """Atributos para cada tipo de log, retornando a mensagem de log. """

    def info(self, message):
        self.log(logging.INFO, message)

    def warning(self, message):
        self.log(logging.WARNING, message)

    def error(self, message, extra=None):
        self.log(logging.ERROR, message)

    def critical(self, message, extra=None):
        self.log(logging.CRITICAL, message)
