from flask import request
from werkzeug.security import generate_password_hash
from app import es_logger
from app import app, require_keys
from app.models.user import User


@app.route('/api/signup', methods=['POST'])
@require_keys(['username', 'password'])
def signup():
    """
    Cria um novo usuário no banco de dados apartir dos dados
    passados no corpo da requisição JSON
    """

    registered_user = User(**request.json)

    if registered_user.validate_user_exists():
        es_logger.warning(f"Usuario: {registered_user.username} já existe")
        return {"message": f"Usuario: {registered_user.username} já existe"}, 400

    # Gera o hash da senha e insere o usuário no banco de dados
    pass_hash = generate_password_hash(registered_user.password)
    registered_user = User(username=registered_user.username, password=pass_hash)
    registered_user.save()
    es_logger.info(f"Usuario: {registered_user.username} criado com sucesso")
    return {"message": f"Usuario: {registered_user.username} criado com sucesso"}, 201
