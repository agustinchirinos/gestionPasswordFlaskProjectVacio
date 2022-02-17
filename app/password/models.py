import os

from cryptography.fernet import Fernet
from werkzeug.security import generate_password_hash, check_password_hash

from app import db


class Usuario(db.Model):
    username = db.Column(db.String(20), primary_key=True)
    password = db.Column(db.String())
    passwordcifrada = db.Column(db.LargeBinary)
    dni = db.Column(db.String(10),nullable=False,unique=True)
    nombre = db.Column(db.String(20),nullable=False)
    apellidos = db.Column(db.String(50),nullable=False)

    def create(self):
        try:
            db.session.add(self)
            db.session.commit()
        except:
            raise

    def update(self):
        try:
            db.session.commit()
        except:
            raise


    def set_password(self, password):
        # self.password = generate_password_hash(password, method='pbkdf2:sha512')
        method = "pbkdf2:sha256:260000"
        # method = "plain"
        # method = "pbkdf2:sha512:1000000"
        self.password = generate_password_hash(password,method=method) #Por defecto sha256
        # self.password = password.split("$", 1)[1]


    def check_password(self, password):
        # passHash = 'pbkdf2:sha256:260000$' + self.password
        return check_password_hash(self.password, password)
