import flask

games = flask.Blueprint("games", __name__)


@games.route('/snake')
def snake():
    return flask.render_template("snake.html")


@games.route('/pong')
def pong():
    return flask.render_template("pong.html")

