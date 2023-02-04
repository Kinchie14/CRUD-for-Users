from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime


class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(50), nullable = False, index = True, unique = True)
    name = db.Column(db.String(50), nullable = False, index = True, unique = True)
    age = db.Column(db.Integer(), nullable = False, index = True, unique = True)
    password_hash = db.Column(db.String(50))

    def __init__(self,email, username, password, name, age):
        self.email = email
        self.username = username
        self.password = password
        self.name = name
        self.age = age
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


    def __repr__(self):
        return f"Username: {self.username}. Name: {self.name}. Age:{self.age}. Email: {self.email}"
    






















