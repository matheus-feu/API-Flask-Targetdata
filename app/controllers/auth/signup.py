from flasgger import swag_from
from flask import request
from werkzeug.security import generate_password_hash

from app import es_logger, app
from app.decorators.required_keys import require_keys
from app.exceptions.missing_json_key_error import MissingJSONKeyError
from app.models.user import User


@app.route('/api/signup', methods=['POST'])
@require_keys(['username', 'password'])
@swag_from('../../docs/signup.yml')
def signup():
    """
    Cria um novo usuário no banco de dados apartir dos dados
    passados no corpo da requisição JSON
    """
    registered_user = User(**request.json)

    if not registered_user.username or not registered_user.password:
        es_logger.warning("Usuário ou senha não informados")
        return {"message": "Usuário ou senha não informados"}, 400

    if registered_user.validate_user_exists():
        es_logger.warning(f"Usuario: {registered_user.username} já existe")
        return {"message": f"Usuario: {registered_user.username} já existe"}, 400

    # Gera o hash da senha e insere o usuário no banco de dados
    pass_hash = generate_password_hash(registered_user.password)
    registered_user = User(username=registered_user.username, password=pass_hash)
    registered_user.save()
    es_logger.info(f"Usuario: {registered_user.username} criado com sucesso")

    return {"message": f"Usuario: {registered_user.username} criado com sucesso"}, 201


@app.errorhandler(MissingJSONKeyError)
def handle_bad_request(error):
    """Trata os erros de requisição JSON."""
    es_logger.warning(f"error: {error.description}")
    message = "Sua requisição JSON não contém um campo obrigatório. Por favor, verifique se a sua requisição contém todos os campos necessários e tente novamente."

    return {'error': message}, 400
