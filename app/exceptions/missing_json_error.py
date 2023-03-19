from werkzeug.exceptions import HTTPException


class MissingJSONKeyError(HTTPException):
    """Clase que representa uma exceção de chave JSON faltando"""
    code = 400
    description = f"A chave é requerida no corpo JSON da requisição, campo invalido!"
