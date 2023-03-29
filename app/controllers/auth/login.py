from datetime import datetime, timedelta

import jwt
from flasgger import swag_from
from flask import request
from werkzeug.security import check_password_hash

from app import es_logger, app
from app.decorators.required_keys import require_keys
from app.models.user import User


@require_keys(['username', 'password'])
@app.route('/api/login', methods=['POST'])
@swag_from('../../docs/login.yml')
def login():
    """Esta função é responsável por validar as credenciais do usuário e
    gerar um token para o usuário acessar os endpoints"""

    # Get the user object from the POST request
    request_login = User(**request.json)

    # Check if user exists
    db_login = request_login.validate_user_exists()

    if db_login:

        # Check if password is correct
        if not check_password_hash(db_login.password, request_login.password):
            es_logger.warning(f"Senha invalida para o usuario: {request_login.username}")
            return {'message': f"Senha invalida para o usuario: {request_login.username}"}, 401

        # Time to expire token
        exp = datetime.utcnow() + timedelta(minutes=app.config['SESSION_EXPIRATE_MINUTES'])

        # Generate an secret token
        secret = app.config['SECRET_KEY']

        security_token = jwt.encode({
            'id': str(db_login.id),
            'exp': exp,
            'username': db_login.username,
        }, secret)
        es_logger.info(f"Usuario: {request_login.username} logado com sucesso")
        es_logger.info('Token gerado com sucesso')
        return {'token': security_token}

    else:
        es_logger.warning(f"Usuario: {request_login.username} não existe")
        return {'message': f"Usuario: {request_login.username} não existe"}, 404


@app.errorhandler(jwt.ExpiredSignatureError)
def handle_expired_token(error):
    """Trata os erros de token expirado."""
    es_logger.warning(f"error: {error.description}")
    return ({'error': f'{str(error)}'}, 401)
