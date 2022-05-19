import flask


def create_app():
    app = flask.Flask(__name__)

    from .games import games
    from .auth import auth
    from .pages import pages

    app.register_blueprint(games, url_prefix='/')
    app.register_blueprint(pages, url_prefix = '/')
    app.register_blueprint(auth, url_prefix='/')

    return app
