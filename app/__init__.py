from flask import Flask

from app.students.views import students_blueprint
from app.extensions import mongo


def created_app(config_settings):
    app = Flask(__name__)
    app.config.from_object(config_settings)

    mongo.init_app(app)
    register_blueprints(app)

    return app


def register_blueprints(app):
    app.register_blueprint(students_blueprint)
