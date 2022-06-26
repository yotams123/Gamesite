import datetime

import flask
import flask_login
import sqlalchemy.exc
import sqlalchemy.orm

import website.models

pages = flask.Blueprint("pages", __name__)


@pages.route('/', methods=['GET', 'POST'])
def home():
    pong_data = website.models.PongScores.query.order_by(website.models.PongScores.score.desc()).all()
    snake_data = website.models.SnakeScores.query.order_by(website.models.SnakeScores.score.desc()).all()

    columns = website.models.columns

    if flask.request.method == 'POST':
        order_col = flask.request.form.get("cols")
        asc_desc = flask.request.form.get("asc_desc")

        if order_col != "":
            snake_data = eval(f"website.models.SnakeScores.query.order_by(website.models.SnakeScores."
                              f"{order_col}.{asc_desc}()).all()")
            pong_data = eval(f"website.models.PongScores.query.order_by(website.models.PongScores."
                             f"{order_col}.{asc_desc}()).all()")

    return flask.render_template("home.html", user=flask_login.current_user, columns=columns,
                                 data_s=snake_data, data_p=pong_data)


@pages.route('/my_scores', methods=['GET', 'POST'])
@flask_login.login_required
def my_scores():
    columns = website.models.columns

    pong_data = website.models.PongScores.query.filter_by(username=flask_login.current_user.username)
    snake_data = website.models.SnakeScores.query.filter_by(username=flask_login.current_user.username)
    if flask.request.method == 'POST':
        if flask.request.form.get("del_row") != "":
            row = int(flask.request.form.get("del_row"))
            table = flask.request.form.get("table")
            table = eval(f"website.models.{table}")
            entry = table.query.filter_by(id=row).first()
            try:
                website.models.db.session.delete(entry)
            except sqlalchemy.orm.exc.UnmappedInstanceError:
                flask.flash("A row with that id does not exist", category="error")
                print(type(row))
                print(type(table.query.first().id))
            website.models.db.session.commit()
        order_col = flask.request.form.get("cols")
        asc_desc = flask.request.form.get("asc_desc")

        if order_col != "":
            snake_data = eval(f"snake_data.order_by(website.models.SnakeScores.{order_col}.{asc_desc}())")
            pong_data = eval(f"pong_data.order_by(website.models.PongScores.{order_col}.{asc_desc}())")
        snake_data = snake_data.all()
        pong_data = pong_data.all()
    return flask.render_template('my_scores.html', user=flask_login.current_user, columns=columns, data_p=pong_data, data_s=snake_data)


@pages.route('/admin', methods=['POST', 'GET'])
@flask_login.login_required
def admin():
    if flask_login.current_user.username != "Ysman":
        flask.redirect(flask.url_for("pages.home"))
    data = website.models.User.query.all()
    if flask.request.method == 'POST':
        if flask.request.form.get('table') is not None:
            table = flask.request.form.get("table")
            table = eval(f"website.models.{table}")
            row = table.query.filter_by(id=flask.request.form.get("del")).first()
            try:
                website.models.db.session.delete(row)
            except sqlalchemy.orm.exc.UnmappedInstanceError:
                flask.flash("A row with that id does not exist in that table", category="error")
            website.models.db.session.commit()
        if flask.request.form.get("update_row") != "":
            row = website.models.User.query.filter_by(id=flask.request.form.get("update_row")).first()
            col = flask.request.form.get("col_name")
            val = flask.request.form.get("col_val")

            for forbidden in ['\'', "\"", "\\", "#"]:
                if forbidden in val:
                    flask.flash("Invalid value", category="error")
                    users_columns = website.models.user_columns
                    return flask.render_template("admin.html", user=flask_login.current_user,
                                                 data=data, users_columns=users_columns)
            try:
                if col == 'birthday':
                    val = datetime.datetime.strptime(val, '%Y-%m-%d').date()
                    exec(f"row.{col} = val")
                else:
                    exec(f"row.{col} = '{val}'")
                website.models.db.session.commit()
            except (sqlalchemy.orm.exc.UnmappedInstanceError, AttributeError, SyntaxError):
                flask.flash("Invalid row or column", category="error")
                website.models.db.session.rollback()
            except ValueError:
                flask.flash("The new value chosen is not a date. Enter a date in '%Y-%m-%d' format, "
                            "as shown in the table", category="error")
                website.models.db.session.rollback()

        order_col = flask.request.form.get("order")
        asc_desc = flask.request.form.get("asc_desc")

        if order_col != "":
            try:
                data = eval(f"website.models.User.query.order_by(website.models.User.{order_col}.{asc_desc}()).all()")
            except (SyntaxError, AttributeError):
                flask.flash("Invalid column to order by", category="error")
    users_columns = website.models.user_columns
    return flask.render_template("admin.html", user=flask_login.current_user, users_columns=users_columns, data=data)
