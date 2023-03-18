from mongoengine import Document, StringField


class User(Document):
    username = StringField(required=True, unique=True)
    password = StringField(required=True)

    def __repr__(self):
        return f'<User {self.username}>'

    def validate_user_exists(self):
        user = User.objects(username=self.username).first()
        return user



