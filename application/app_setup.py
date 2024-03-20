import flask
import __main__

__main__.app = app = flask.Flask(__main__.__name__)

app.config.update({
    'DEBUG': True,
    'PORT': 5000,
    'HOST': 'localhost',
    'SECRET_KEY': 'secret',
    'SQLALCHEMY_DATABASE_URI': 'sqlite:///chat.db',
    'SQLALCHEMY_TRACK_MODIFICATIONS': False,
})

del __main__

route = app.route
render_template = flask.render_template
render_template_string = flask.render_template_string
request = flask.request
session = flask.session
url_for = flask.url_for
