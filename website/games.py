import flask
import flask_login
import datetime

import website.models

games = flask.Blueprint("games", __name__)


@games.route('/snake', methods=['GET', 'POST'])
@flask_login.login_required
def snake():
    if flask.request.method == 'POST':
        score = flask.request.form.get('score')
        log = website.models.SnakeScores(username=flask_login.current_user.username, score=score)
        website.models.db.session.add(log)
        website.models.db.session.commit()
    return flask.render_template("snake.html", user=flask_login.current_user)


@games.route('/pong', methods=['GET', 'POST'])
@flask_login.login_required
def pong():
    if flask.request.method == 'POST':
        score = flask.request.form.get('score')
        log = website.models.PongScores(username=flask_login.current_user.username, score=score)
        website.models.db.session.add(log)
        website.models.db.session.commit()
    return flask.render_template("pong.html", user=flask_login.current_user)


@games.route('/space-invaders', methods=['GET', 'POST'])
@flask_login.login_required
def space_invaders():
    if flask.request.method == 'POST':
        score = flask.request.form.get('score')
        log = website.models.SpaceInvadersScores(username=flask_login.current_user.username, score=score)
        website.models.db.session.add(log)
        website.models.db.session.commit()
    return flask.render_template("invaders.html", user=flask_login.current_user)
