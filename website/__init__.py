import flask
import flask_sqlalchemy
import flask_login
import os

db = flask_sqlalchemy.SQLAlchemy()
DB_NAME = "gamesiteDB.db"


def create_app():
    app = flask.Flask(__name__)
    app.config['SECRET_KEY'] = 'ksjhdfkhsdkjfhk'
    app.config["SQLALCHEMY_DATABASE_URI"] =f"sqlite:///{DB_NAME}"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)

    from .games import games
    from .auth import auth
    from .pages import pages

    app.register_blueprint(games, url_prefix='/')
    app.register_blueprint(pages, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from website.models import User

    create_database(app)

    login_manager = flask_login.LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app


def create_database(app):
    if not os.path.exists("/website/" + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')
