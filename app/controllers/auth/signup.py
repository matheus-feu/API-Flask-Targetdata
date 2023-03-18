from flask import request
from werkzeug.security import generate_password_hash
from app import app, require_keys
from app.models.user import User


@app.route('/signup', methods=['POST'])
@require_keys(['username', 'password'])
def signup():
    registered_user = User(**request.json)

    if registered_user.validate_user_exists():
        return {"message": "User already exists"}, 400

    # Gera o hash da senha e insere o usuário no banco de dados
    pass_hash = generate_password_hash(registered_user.password)
    registered_user = User(username=registered_user.username, password=pass_hash)
    registered_user.save()

    return {"message": "User created successfully"}, 201
