from flask import Flask


def create_app():

    app = Flask(__name__)
    app.add_url_rule('/', endpoint='index')

    from .accounts.urls import accounts
    from .blogs.urls import blogs
    app.register_blueprint(accounts)
    app.register_blueprint(blogs)

    return app
