from . import db
import flask_login
import sqlalchemy


class User(db.Model, flask_login.UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    username = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(50))
    email = db.column(db.String(50), unique=True)
    birthday = db.Column(db.Date(timezone=True), default=sqlalchemy.sql.func.now())
    location = db.Column(db.String(50))
    gender = db.Column(db.String(6))
    snake_scores = db.relationship('SnakeScores')
    pong_scores = db.relationship('PongScores')


class SnakeScores(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), db.ForeignKey('user.username'))
    score = db.Column(db.Integer)
    date = db.Column(db.DateTime(timezone=True), default=sqlalchemy.sql.func.now())


class PongScores(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), db.ForeignKey('user.username'))
    score = db.Column(db.Integer)
    date = db.Column(db.DateTime(timezone=True), default=sqlalchemy.sql.func.now())
