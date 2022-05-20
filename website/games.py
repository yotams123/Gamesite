import flask

games = flask.Blueprint("games", __name__)


@games.route('/snake')
def snake():
    pass


@games.route('/pong')
def pong():
    pass

