import flask
import werkzeug.security
import website.models
import datetime

auth = flask.Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if flask.request.method == 'POST':
        username = flask.request.form.get("user")
        password = flask.request.form.get("password")
        flask.flash("Successfully logged in!", category="success")
    return flask.render_template("login.html")


@auth.route('/register', methods=['GET', 'POST'])
def register():
    print(flask.request.method)
    if flask.request.method == "POST" and flask.request.form.get("submit") is not None:
        print(flask.request.form.get("submit"))
        firstname = flask.request.form.get("firstname")
        lastname = flask.request.form.get("lastname")
        username = flask.request.form.get("new_user")
        password = flask.request.form.get("new_pass")
        email = flask.request.form.get("mail")
        birthday = flask.request.form.get("birthday")
        location = flask.request.form.get("loc")
        gender = flask.request.form.get("gender")

        new_user = website.models.User(first_name=firstname, last_name=lastname, username=username,
                                       password=werkzeug.security.generate_password_hash(password, method='sha256'),
                                       email=email,
                                       birthday=datetime.datetime.strptime(birthday, '%Y-%m-%d').date(), location=location, gender=gender)
        website.models.db.session.add(new_user)
        website.models.db.session.commit()
        flask.flash("Successfully registered!", category="success")
        return flask.redirect(flask.url_for('pages.home'))
    return flask.render_template("register.html")


@auth.route('/my-account', methods=['GET', 'POST'])
def my_account():
    if flask.request.method == 'POST':
        firstname = flask.request.form.get("firstname")
        lastname = flask.request.form.get("lastname")
        username = flask.request.form.get("new_user")
        old_password = flask.request.form.get("pass")
        new_password = flask.request.form.get("new_pass")
        email = flask.request.form.get("mail")
        birthday = flask.request.form.get("birthday")
        location = flask.request.form.get("loc")
        gender = flask.request.form.get("gender")
        flask.flash("Successfully updated user info!", "success")
    return flask.render_template("my_account.html")
