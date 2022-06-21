import flask_login
from . import db
import sqlalchemy


class User(db.Model, flask_login.UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    birthday = db.Column(db.Date(), nullable=False)
    location = db.Column(db.String(50), nullable=False)
    gender = db.Column(db.String(6), nullable=False)

    snake_scores = db.relationship('SnakeScores', backref='user', lazy='dynamic')
    pong_scores = db.relationship('PongScores', backref='user', lazy='dynamic')


user_columns = ['id', 'first_name', 'last_name', 'username', 'email', 'birthday', 'location', 'gender']


class SnakeScores(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), db.ForeignKey('user.username'), nullable=False)
    score = db.Column(db.Integer, nullable=False)
    date = db.Column(db.DateTime(), default=sqlalchemy.sql.func.now())


snake_columns = ['id', 'username', 'score', 'date']


class PongScores(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), db.ForeignKey('user.username'), nullable=False)
    score = db.Column(db.Integer, nullable=False)
    date = db.Column(db.DateTime(), default=sqlalchemy.sql.func.now(), nullable=False)


pong_columns = ['id', 'username', 'score', 'date']
