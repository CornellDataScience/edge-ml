from flask_login import UserMixin


# User class for flask-login
class User(UserMixin):
    def __init__(self, email, password):
        self.id = email
        self.password = password
