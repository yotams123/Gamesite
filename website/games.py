import flask
import flask_login
import datetime

from website.models import *

games = flask.Blueprint("games", __name__)


@games.route('/snake', methods=['GET', 'POST'])
@flask_login.login_required
def snake():
    if flask.request.method == 'POST':
        score = flask.request.form.get('score')
        log = SnakeScores(username=flask_login.current_user.username, score=score)
        db.session.add(log)
        db.session.commit()
    return flask.render_template("snake.html", user=flask_login.current_user)


@games.route('/pong', methods=['GET', 'POST'])
@flask_login.login_required
def pong():
    if flask.request.method == 'POST':
        score = flask.request.form.get('score')
        log = PongScores(username=flask_login.current_user.username, score=score)
        db.session.add(log)
        db.session.commit()
    return flask.render_template("pong.html", user=flask_login.current_user)


@games.route('/space-invaders', methods=['GET', 'POST'])
@flask_login.login_required
def space_invaders():
    if flask.request.method == 'POST':
        score = flask.request.form.get('score')
        log = SpaceInvadersScores(username=flask_login.current_user.username, score=score)
        db.session.add(log)
        db.session.commit()
    return flask.render_template("invaders.html", user=flask_login.current_user)
