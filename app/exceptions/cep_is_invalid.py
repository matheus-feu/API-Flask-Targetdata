from werkzeug.exceptions import HTTPException


class CEPInvalidException(HTTPException):
    code = 400
    description = "O CEP informado é inválido"
