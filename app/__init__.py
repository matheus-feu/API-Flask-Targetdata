from flask import Flask
from flask_jwt_extended import JWTManager
from flask_mongoengine import MongoEngine

from app.utils.elasticsearch_logs import ElasticSearchLogger
from config.model_elasticseach_log import LoggerConfigElasticsearch
from flasgger import Swagger

es_logger = ElasticSearchLogger(
    index_name=LoggerConfigElasticsearch.index_name,
    elasticsearch_host=LoggerConfigElasticsearch.host)


def create_app():
    """Função responsável pela criação e instância do app Flask."""
    app = Flask(__name__)
    app.config.from_object('config')
    app.config['MONGODB_SETTINGS'] = {
        'db': 'test',
        'host': 'localhost',
        'port': 27017
    }
    swagger = Swagger(app, template_file='doc.yml')

    jwt = JWTManager(app)
    db = MongoEngine(app)

    return app


# Rotas do app
from app.controllers.auth.login import *
from app.controllers.auth.signup import *
from app.controllers.cep.weather_address import *
from app.controllers.logs.requests_info_logs import *
