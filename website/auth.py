import flask

auth = flask.Blueprint('auth', __name__)


@auth.route('/login')
def login():
    return flask.render_template("login.html")


@auth.route('/register')
def register():
    return flask.render_template("register.html")


@auth.route('/my-account')
def my_account():
    return flask.render_template("my_account.html")
