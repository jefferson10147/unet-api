from flask import Flask

from app.students.views import students_blueprint
from app.users.views import users_blueprint
from app.extensions import mongo, jwt
from app.settings import Production
from app.views import main


def create_app(config_settings=Production):
    app = Flask(__name__)
    app.config.from_object(config_settings)

    register_extensions(app)
    register_blueprints(app)

    return app


def register_blueprints(app):
    app.register_blueprint(main)
    app.register_blueprint(users_blueprint)
    app.register_blueprint(students_blueprint)


def register_extensions(app):
    mongo.init_app(app)
    jwt.init_app(app)