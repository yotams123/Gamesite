import datetime

import flask
import flask_login

import website.models

pages = flask.Blueprint("pages", __name__)


@pages.route('/')
def home():
    snake_columns = website.models.snake_columns
    snake_data = website.models.SnakeScores.query.order_by(website.models.SnakeScores.score.desc()).all()

    pong_columns = website.models.pong_columns
    pong_data = website.models.PongScores.query.order_by(website.models.PongScores.score.desc()).all()

    return flask.render_template("home.html", user=flask_login.current_user, columns_s=snake_columns,
                                 data_s=snake_data, columns_p=pong_columns, data_p=pong_data)


@pages.route('/admin', methods=['GET', 'POST'])
def admin():
    data = website.models.User.query.all()
    users_columns = website.models.user_columns
    if flask.request.method == 'POST':
        if flask.request.form.get('table') is not None:
            table = flask.request.form.get("table")
            table = eval(f"website.models.{table}")
            row = table.query.filter_by(id=flask.request.form.get("del")).first()
            website.models.db.session.delete(row)
            website.models.db.session.commit()
    return flask.render_template("admin.html", user=flask_login.current_user, data=data, users_columns=users_columns)
