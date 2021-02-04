from flask import Flask

from app.students.views import students_blueprint

def created_app(config_settings):
    app = Flask(__name__)
    app.config.from_object(config_settings)
    register_blueprints(app)

    return app


def register_blueprints(app):
    app.register_blueprint(students_blueprint)
