from werkzeug.exceptions import HTTPException


class MissingJSONKeyError(HTTPException):
    code = 400
    description = f"A chave é requerida no corpo JSON da requisição, campo invalido!"
