from datetime import datetime, timedelta

import jwt
from flask import request
from werkzeug.security import check_password_hash

from app import app
from app.decorators.required_keys import require_keys
from app.models.user import User



@app.route('/login', methods=['GET'])
@require_keys(['username', 'password'])
def login():
    request_login = User(**request.json)

    db_login = request_login.validate_user_exists()

    if db_login:

        if not check_password_hash(db_login.password, request_login.password):
            return {'message': 'Invalid username or password'}, 401

        exp = datetime.utcnow() + timedelta(minutes=app.config['SESSION_EXPIRATE_MINUTES'])

        secret = app.config['SECRET_KEY']

        security_token = jwt.encode({
            'id': str(db_login.id),
            'exp':exp,
            'username': db_login.username,
        },secret)

        return {'token': security_token}

    else:
        return {'message': 'User does not exist'}, 404
