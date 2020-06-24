from flask import Flask

from .accounts.urls import accounts
from .blogs.urls import blogs


def create_app():

    app = Flask(__name__)

    app.register_blueprint(accounts)
    app.register_blueprint(blogs)

    return app
