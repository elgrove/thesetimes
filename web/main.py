from flask import Flask
from core import core

app = Flask(__name__)


def create_app():
    app = Flask(__name__)
    app.register_blueprint(core)
    return app
