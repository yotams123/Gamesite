import datetime

import flask
import flask_login
import sqlalchemy.exc
import sqlalchemy.orm

from website.models import *

pages = flask.Blueprint("pages", __name__)


@pages.route('/', methods=['GET', 'POST'])
def home():
    pong_data = PongScores.query.order_by(PongScores.score.desc()).all()
    snake_data = SnakeScores.query.order_by(SnakeScores.score.desc()).all()
    invaders_data = SpaceInvadersScores.query.order_by(SpaceInvadersScores.score.desc()).all()

    if flask.request.method == 'POST':
        order_col = flask.request.form.get("cols")
        asc_desc = flask.request.form.get("asc_desc")

        if order_col in columns and asc_desc in ["asc", "desc"]:
            snake_data = eval(f"SnakeScores.query.order_by(SnakeScores.{order_col}.{asc_desc}()).all()")
            pong_data = eval(f"PongScores.query.order_by(PongScores.{order_col}.{asc_desc}()).all()")
            invaders_data = eval(f"SpaceInvadersScores.query.order_by(SpaceInvadersScores."
                                 f"{order_col}.{asc_desc}()).all()")

    return flask.render_template("home.html", user=flask_login.current_user, columns=columns,
                                 data_s=snake_data, data_p=pong_data, data_i=invaders_data)


@pages.route('/my_scores', methods=['GET', 'POST'])
@flask_login.login_required
def my_scores():

    pong_data = PongScores.query.filter_by(username=flask_login.current_user.username)
    snake_data = SnakeScores.query.filter_by(username=flask_login.current_user.username)
    invaders_data = SpaceInvadersScores.query.filter_by(username=flask_login.current_user.username)

    if flask.request.method == 'POST':

        if flask.request.form.get("del_row").isnumeric():
            row = int(flask.request.form.get("del_row"))
            table = flask.request.form.get("table")
            if table in models:
                table = eval(f"{table}")
                entry = table.query.filter_by(id=row).first()

                try:
                    db.session.delete(entry)

                except sqlalchemy.orm.exc.UnmappedInstanceError:
                    flask.flash("A row with that id does not exist", category="error")
                    print(type(row))
                    print(type(table.query.first().id))

            db.session.commit()

        order_col = flask.request.form.get("cols")
        asc_desc = flask.request.form.get("asc_desc")

        if order_col in columns and asc_desc in ["asc", "desc"]:
            snake_data = eval(f"snake_data.order_by(SnakeScores.{order_col}.{asc_desc}())")
            pong_data = eval(f"pong_data.order_by(PongScores.{order_col}.{asc_desc}())")
            invaders_data = eval(f"invaders_data.order_by(SpaceInvadersScores.{order_col}.{asc_desc}())")

        snake_data = snake_data.all()
        pong_data = pong_data.all()
        invaders_data = invaders_data.all()

    return flask.render_template('my_scores.html', user=flask_login.current_user, columns=columns, data_p=pong_data,
                                 data_s=snake_data, data_i=invaders_data)


@pages.route('/admin', methods=['POST', 'GET'])
@flask_login.login_required
def admin():

    admins = ["Ysman", "YotamS123"]
    users_columns = user_columns
    if flask_login.current_user.username not in admins:
        flask.redirect(flask.url_for("pages.home"))
    data = User.query.all()
    if flask.request.method == 'POST':
        if flask.request.form.get('table') in models:
            table = flask.request.form.get("table")
            table = eval(f"{table}")
            row = table.query.filter_by(id=flask.request.form.get("del")).first()
            try:
                db.session.delete(row)
            except sqlalchemy.orm.exc.UnmappedInstanceError:
                flask.flash("A row with that id does not exist in that table", category="error")
            db.session.commit()
        if flask.request.form.get("update_row").isnumeric():
            row = User.query.filter_by(id=flask.request.form.get("update_row")).first()
            col = flask.request.form.get("col_name")
            val = flask.request.form.get("col_val")

            for forbidden in ['\'', "\"", "\\", "#"]:
                if forbidden in val:
                    flask.flash("Invalid value", category="error")
                    users_columns = user_columns
                    return flask.render_template("admin.html", user=flask_login.current_user,
                                                 data=data, users_columns=users_columns)
            try:
                if col == 'birthday':
                    val = datetime.datetime.strptime(val, '%Y-%m-%d').date()
                    exec(f"row.{col} = val")
                elif col in users_columns:
                    exec(f"row.{col} = '{val}'")
                db.session.commit()
            except (sqlalchemy.orm.exc.UnmappedInstanceError, AttributeError, SyntaxError):
                flask.flash("Invalid row or column", category="error")
                db.session.rollback()
            except ValueError:
                flask.flash("The new value chosen is not a date. Enter a date in '%Y-%m-%d' format, "
                            "as shown in the table", category="error")
                db.session.rollback()

        order_col = flask.request.form.get("order")
        asc_desc = flask.request.form.get("asc_desc")

        if order_col in users_columns:
            data = eval(f"User.query.order_by(User.{order_col}.{asc_desc}()).all()")

    return flask.render_template("admin.html", user=flask_login.current_user, users_columns=users_columns, data=data)
