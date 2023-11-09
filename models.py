from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    # id uses uuid4 to generate a unique id
    id = db.Column(db.String(36), primary_key=True)
    username = db.Column(db.String(20), unique=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(60))
    role = db.Column(db.String(20), default='user')
