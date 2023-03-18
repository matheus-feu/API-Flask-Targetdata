from functools import wraps

from flask import request

from app.exceptions.json_payload_error import JSONPayloadError
from app.exceptions.missing_json_error import MissingJSONKeyError


def require_keys(keys):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):

            if not request.is_json:
                raise JSONPayloadError()

            data_request = request.get_json()

            for key_value in keys:
                if key_value not in data_request:
                    raise MissingJSONKeyError(key_value)

            return func(*args, **kwargs)

        return wrapper

    return decorator
