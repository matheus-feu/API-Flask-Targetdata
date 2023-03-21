import os

from flasgger import Swagger
from flask import Flask
from flask_jwt_extended import JWTManager
from flask_mongoengine import MongoEngine

from app.config.swagger import swagger_config, template
from app.models.elasticseach_log import LoggerConfigElasticsearch
from app.utils.elasticsearch_logs import ElasticSearchLogger

# Instanciando a aplicação
app = Flask(__name__)

# Configuração da aplicação
app.config.from_object('config')

# Configuração do banco de dados
app.config['MONGODB_SETTINGS'] = {
    'db': app.config['MONGODB_NAME'],
    'host': os.environ.get('MONGODB_HOST'),
    'port': int(os.environ.get('MONGODB_PORT'))
}

db = MongoEngine(app)

# Configuração da documentação Swagger
swagger = Swagger(app, config=swagger_config, template=template)

# Configuração do JWT
jwt = JWTManager(app)

# Instanciando a classe de logs
es_logger = ElasticSearchLogger(
    index_name=LoggerConfigElasticsearch.index_name,
    elasticsearch_host=LoggerConfigElasticsearch.host)

# Rotas da aplicação
from app.controllers.auth.login import *
from app.controllers.auth.signup import *
from app.controllers.cep.weather_address import *
from app.controllers.logs.requests_info_logs import *
