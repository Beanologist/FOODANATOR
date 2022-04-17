from flask import Flask, url_for


def createApp():
    app = Flask(__name__)
    from .routes import page
    app.register_blueprint(page, url_prefix='/')
    return app
