from werkzeug.exceptions import HTTPException


class JSONPayloadError(HTTPException):
    code = 400
    description = "A requisição precisa incluir um payload em formato JSON"
