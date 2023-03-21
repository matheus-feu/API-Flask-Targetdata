import pytest
from pymongo import MongoClient
from werkzeug.security import generate_password_hash

from app import app
from app.models.user import User


@pytest.fixture()
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


@pytest.fixture()
def mongo_db():
    client = MongoClient('mongodb://localhost:27017/')
    db = client['test_database']
    yield db
    client.drop_database('test_database')


def test_insert_user(mongo_db):
    collection = mongo_db['test_collection']
    doc = {'name': 'teste', 'password': 'teste123'}
    result = collection.insert_one(doc)
    assert result.inserted_id is not None


def test_login_with_correct_credentials(app, mongo_db):
    # Preparação
    client = app.client
    user_data = {
        "username": "test",
        "password": "teste123"
    }
    user = User(**user_data)
    user.password = generate_password_hash(user.password)
    user.save()

    # Teste com credenciais corretas
    response = client.post('/api/login', json=user_data)

    assert response.status_code == 200
    assert 'token' in response.json
    assert response.json['token'] is not None


def test_login_with_wrong_password(app, mongo_db):
    # Preparação
    client = app.client
    user_data = {
        "username": "test_user",
        "password": "password"
    }
    user = User(**user_data)
    user.password = generate_password_hash(user.password)
    user.save()

    # Teste com senha incorreta
    response = client.post('/api/login', json={"username": "test_user", "password": "wrong_password"})

    assert response.status_code == 401
    assert response.json['message'] == 'Senha invalida para o usuario: test_user'


def test_login_with_non_existing_user(app, mongo_db):
    # Preparação
    client = app.client

    # Teste com usuário inexistente
    response = client.post('/api/login', json={"username": "test_user", "password": "password"})

    assert response.status_code == 404
    assert response.json['message'] == 'Usuario: test_user não existe'
