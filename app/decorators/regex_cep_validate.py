import re
from functools import wraps

from flask import request
from app import es_logger
from app.exceptions.cep_is_invalid import CEPInvalidException


def regex_cep_validate(func):
    """Esta função é um decorator que há um regex que valida o CEP informado pelo usuário.
    Este regex só aceita 8 dígitos, sem traços ou pontos."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        cep = request.json['cep']

        regex_cep = re.compile(r'^\d{8}$')

        if not regex_cep.match(cep):
            es_logger.warning('CEP is invalid')
            raise CEPInvalidException()

        es_logger.info('CEP is valid')
        return func(*args, **kwargs)

    return wrapper
