from mongoengine import Document, StringField


class User(Document):
    """Classe que representa um usuário no banco de dados, há métodos que valida se o usuário já existe e retorna o usuário"""
    username = StringField(required=True, unique=True)
    password = StringField(required=True)

    def __repr__(self):
        return f'<User {self.username}>'

    def validate_user_exists(self):
        user = User.objects(username=self.username).first()
        return user



