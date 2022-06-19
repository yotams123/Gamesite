import flask
import werkzeug.security
import website.models
import datetime
import flask_login

auth = flask.Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if flask.request.method == 'POST':
        username = flask.request.form.get("user")
        password = flask.request.form.get("password")
        user = website.models.User.query.filter_by(username=username).first()
        if user:
            if werkzeug.security.check_password_hash(user.password, password):
                flask_login.login_user(user)
                flask.flash("Successfully logged in!", category="success")
                return flask.redirect(flask.url_for('pages.home'))
        flask.flash("Password or Username invalid", category="error")
    return flask.render_template("login.html")


@auth.route('/register', methods=['GET', 'POST'])
def register():
    if flask.request.method == "POST":
        firstname = flask.request.form.get("firstname")
        lastname = flask.request.form.get("lastname")
        username = flask.request.form.get("new_user")
        password = flask.request.form.get("new_pass")
        email = flask.request.form.get("mail")
        birthday = flask.request.form.get("birthday")
        location = flask.request.form.get("loc")
        gender = flask.request.form.get("gender")

        user = website.models.User.query.filter_by(username=username).first()
        if user:
            flask.flash("User already exists with that name", category='error')
        else:
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
@flask_login.login_required
def my_account():
    if flask.request.method == 'POST':
        # if flask.request.form.get('submit'):
        #     firstname = flask.request.form.get("firstname")
        #     lastname = flask.request.form.get("lastname")
        #     username = flask.request.form.get("new_user")
        #     old_password = flask.request.form.get("pass")
        #     new_password = flask.request.form.get("new_pass")
        #     email = flask.request.form.get("mail")
        #     birthday = flask.request.form.get("birthday")
        #     location = flask.request.form.get("loc")
        #     gender = flask.request.form.get("gender")
        #     flask.flash("Successfully updated user info!", "success")
        if flask.request.form.get('logout'):
            flask_login.logout_user()
            return flask.redirect(flask.url_for('auth.login'))
    return flask.render_template("my_account.html")
