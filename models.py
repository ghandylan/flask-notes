from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    # id uses uuid4 to generate a unique id
    user_id = db.Column(db.String(36), primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    role = db.Column(db.String(20), default='user', nullable=False)

    def get_id(self):
        return self.user_id


class Note(db.Model):
    __tablename__ = 'notes'
    # id uses uuid4 to generate a unique id
    note_id = db.Column(db.String(36), primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text)
    date_created = db.Column(db.DateTime)
    favorite = db.Column(db.Boolean, default=False)
    user_id = db.Column(db.String(36), db.ForeignKey('users.user_id'))
    user = db.relationship('User', backref=db.backref('notes', lazy=True))
