from .app_setup import *
from .plugins import *


def run():
    plugins.init_app(app)
    socketio.run(app, allow_unsafe_werkzeug=True)
    
    