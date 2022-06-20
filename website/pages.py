import flask
import flask_login

import website.models

pages = flask.Blueprint("pages", __name__)


@pages.route('/')
def home():
    snake_columns = website.models.snake_columns
    snake_data = website.models.SnakeScores.query.all()
    pong_columns = website.models.pong_columns
    pong_data = website.models.PongScores.query.all()
    return flask.render_template("home.html", user=flask_login.current_user, columns_s=snake_columns,
                                 data_s=snake_data, columns_p=pong_columns, data_p=pong_data)


@pages.route('/admin')
def admin():
    data = website.models.User.query.all()
    users_columns = website.models.user_columns
    return flask.render_template("admin.html", user=flask_login.current_user, data=data, users_columns=users_columns)
