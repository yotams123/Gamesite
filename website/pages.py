import flask

pages = flask.Blueprint("pages", __name__)

@pages.route('/')
def home():
    pass

@pages.route('/admin')
def admin():
    pass
