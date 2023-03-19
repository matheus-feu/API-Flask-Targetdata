from werkzeug.exceptions import HTTPException


class CEPInvalidException(HTTPException):
    """Clase que representa uma exceção de CEP inválido"""
    code = 400
    description = "O CEP informado é inválido"
