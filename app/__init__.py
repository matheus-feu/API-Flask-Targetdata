from flask import Flask
from flask_jwt_extended import JWTManager
from flask_mongoengine import MongoEngine


# logging.basicConfig(filename='record.log', level=logging.DEBUG)

# swagger = Swagger(app, template_file='wrapper.yml')

def create_app():
    """Construct the core application."""
    app = Flask(__name__)
    app.config.from_object('config')
    app.config['MONGODB_SETTINGS'] = {
        'db': 'test',
        'host': 'localhost',
        'port': 27017
    }

    jwt = JWTManager(app)
    db = MongoEngine(app)

    return app


from app.controllers.auth.login import *
from app.controllers.auth.signup import *
from app.controllers.cep.weather_address import *
