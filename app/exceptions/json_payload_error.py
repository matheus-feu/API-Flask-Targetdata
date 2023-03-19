from werkzeug.exceptions import HTTPException


class JSONPayloadError(HTTPException):
    """Clase que representa uma exceção de payload JSON inválido"""
    code = 400
    description = "A requisição precisa incluir um payload em formato JSON"
