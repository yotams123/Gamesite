import flask
import flask_sqlalchemy

db = flask_sqlalchemy.SQLAlchemy()
DB_NAME = "gamesiteDB.db"


def create_app():
    app = flask.Flask(__name__)
    app.config['SECRET_KEY'] = 'ksjhdfkhsdkjfhk'
    app.config["SQLALCHEMY_DATABASE_URI"] =f"sqlite:///{DB_NAME}"
    db.init_app(app)

    from .games import games
    from .auth import auth
    from .pages import pages

    app.register_blueprint(games, url_prefix='/')
    app.register_blueprint(pages, url_prefix = '/')
    app.register_blueprint(auth, url_prefix='/')

    return app
