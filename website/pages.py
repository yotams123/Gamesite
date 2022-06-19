import flask
import flask_login

import website.models

pages = flask.Blueprint("pages", __name__)


@pages.route('/')
def home():
    return flask.render_template("home.html", user=flask_login.current_user)


@pages.route('/admin')
def admin():
    data = website.models.User.query.all()
    users_columns = website.models.user_columns
    return flask.render_template("admin.html", user=flask_login.current_user, data=data, users_columns=users_columns)
