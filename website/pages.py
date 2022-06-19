import flask
import flask_login

pages = flask.Blueprint("pages", __name__)


@pages.route('/')
def home():
    return flask.render_template("home.html", user=flask_login.current_user)


@pages.route('/admin')
def admin():
    return flask.render_template("admin.html", user=flask_login.current_user)
