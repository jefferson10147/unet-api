from flask import Flask


def created_app(config_settings):
    app = Flask(__name__)
    app.config.from_object(config_settings)
    return app
