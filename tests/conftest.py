import pytest

from app import app


@pytest.fixture(scope="module")
def app():
    return app


@pytest.fixture()
def cep():
    cep = '01001000'
    return cep


@pytest.fixture()
def config():
    return config
