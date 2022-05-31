import flask

games = flask.Blueprint("games", __name__)


@games.route('/snake')
def snake():
    flask.render_template("snake.html")


@games.route('/pong')
def pong():
    pass

