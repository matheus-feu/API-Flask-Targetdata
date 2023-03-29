from werkzeug.exceptions import HTTPException


class MissingJSONKeyError(HTTPException):
    """Clase que representa uma exceção das keys(JSON) faltando"""
    code = 400
    description = "A chave é requerida no corpo JSON da requisição, campo invalido!"
