from app import create_app
from app.models.user import User

app = create_app()


def test_db_connected():
    """Testa se o banco de dados está conectado"""
    db_config = app.config['MONGODB_SETTINGS']

    assert db_config['db'] == 'test'


def test_user_exists():
    """Vai consultar o banco de dados e verificar se o usuário existe"""

    user = User.objects(username='admin').first()
    assert user is not None
