import flask

auth = flask.Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    return flask.render_template("login.html")


@auth.route('/register', methods=['GET', 'POST'])
def register():
    return flask.render_template("register.html")


@auth.route('/my-account', methods=['GET', 'POST'])
def my_account():
    return flask.render_template("my_account.html")
