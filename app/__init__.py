import logging

from flask import Flask
from flask_jwt_extended import JWTManager
from flask_mongoengine import MongoEngine

# logging.basicConfig(filename='record.log', level=logging.DEBUG)

app = Flask(__name__)
app.config.from_object('config')

app.config['MONGODB_SETTINGS'] = {
    'db': 'test',
    'host': 'localhost',
    'port': 27017
}

db = MongoEngine(app)

jwt = JWTManager(app)

# swagger = Swagger(app, template_file='wrapper.yml')

from app.controllers.auth.login import *
from app.controllers.auth.signup import *
from app.controllers.cep.weather_address import *

a = 1
