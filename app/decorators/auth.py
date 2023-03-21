from functools import wraps

import jwt
from flask import request

from app import es_logger, app
from app.models.user import User


def token_required():
    def decorator(function):
        """Esta função é um decorator que verifica se o token passado no header da requisição é válido."""

        @wraps(function)
        def wrapper(*args, **kwargs):
            """Esta função é um wrapper que verifica se o token passado no header da requisição é válido.
            Se o token for válido, o usuário é passado como parâmetro para a função que vai ser decorada."""

            token = None

            # verificar se a chave x-access-token existe
            if not "x-access-token" in request.headers:
                es_logger.warning("Key x-access-token is missing!")
                return "Key x-access-token is missing!", 400

            # capturar o token da chave x-access-token
            token = request.headers['x-access-token']

            try:
                # decodificar o token
                # verificar se o token é válido
                data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
                es_logger.info("Token is valid!")
            except jwt.ExpiredSignatureError:
                es_logger.warning("Session Expired!")
                return "Session Expired", 401

            except:
                es_logger.warning("Invalid token!")
                return "Invalid token!", 401

            # verificar se o usuário existe
            # data['username'] = username do usuário
            current_user = User(username=data['username'])
            current_user = current_user.validate_user_exists()

            # parametro current_user é passado para a função que vai ser decorada
            kwargs["current_user"] = current_user

            return function(*args, **kwargs)

        return wrapper

    return decorator
