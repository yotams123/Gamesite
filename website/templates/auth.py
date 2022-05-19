import flask

auth = flask.Blueprint('auth', __name__)

@auth.route('/login')
def login():
    pass

@auth.route('/register')
def register():
    pass

@auth.route('/my-account')
def my_account():
    pass
