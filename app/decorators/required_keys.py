from functools import wraps

from flask import request

from app import es_logger
from app.exceptions.json_payload_error import JSONPayloadError
from app.exceptions.missing_json_key_error import MissingJSONKeyError


def require_keys(keys):
    """Essa função é um decorador que verifica se as chaves estão no json da requisição."""

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            """Nesta função recebe os argumentos e verifica se as chaves estão no json da requisição."""

            if not request.is_json:
                raise JSONPayloadError()

            data_request = request.get_json()

            for key_value in keys:
                if key_value not in data_request:
                    es_logger.warning(f"Key {key_value} is missing!")
                    raise MissingJSONKeyError(key_value)

            return func(*args, **kwargs)

        return wrapper

    return decorator
