import flask
import flask_login

games = flask.Blueprint("games", __name__)


@games.route('/snake')
@flask_login.login_required
def snake():
    return flask.render_template("snake.html", user=flask_login.current_user)


@games.route('/pong')
@flask_login.login_required
def pong():
    return flask.render_template("pong.html", user=flask_login.current_user)

