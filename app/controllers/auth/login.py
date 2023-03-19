from datetime import datetime, timedelta

import jwt
from flask import request
from werkzeug.security import check_password_hash

from app import create_app
from app.decorators.required_keys import require_keys
from app.models.user import User

app = create_app()

@app.route('/login', methods=['POST'])
@require_keys(['username', 'password'])
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
            return {'message': 'Invalid username or password'}, 401

        # Time to expire token
        exp = datetime.utcnow() + timedelta(minutes=app.config['SESSION_EXPIRATE_MINUTES'])

        # Generate an secret token
        secret = app.config['SECRET_KEY']

        security_token = jwt.encode({
            'id': str(db_login.id),
            'exp': exp,
            'username': db_login.username,
        }, secret)

        return {'token': security_token}

    else:
        return {'message': 'User does not exist'}, 404
