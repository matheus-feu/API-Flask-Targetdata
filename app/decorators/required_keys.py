from functools import wraps

from flask import request

from app.exceptions.json_payload_error import JSONPayloadError


def require_keys(keys):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):

            if not request.is_json:
                raise JSONPayloadError()

            data_request = request.get_json()

            for key_value in keys:
                if key_value not in data_request:
                    return {
                        "message": f"A chave '{key_value}' é requerida no corpo JSON da requisição, campo invalido!"}

            return func(*args, **kwargs)

        return wrapper

    return decorator
