from functools import wraps

import jwt
from flask import request

from app import app
from app.models.user import User


def token_required():
    def decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):

            token = None

            # verificar se a chave x-access-token existe
            if not "x-access-token" in request.headers:
                return "Key x-access-token is missing!", 400

            # capturar o token da chave x-access-token
            token = request.headers['x-access-token']

            try:
                # decodificar o token
                # verificar se o token é válido
                data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
            except jwt.ExpiredSignatureError:
                return "Session Expired", 401
            except:
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
