from bson import json_util
from flask import Blueprint, Response

from .models import StudentsModel


students_blueprint = Blueprint(
    name="students",
    import_name=__name__,
    url_prefix="/api/students"
)
students_model = StudentsModel()


@students_blueprint.route('/')
def student_hi():
    db_response = students_model.get_all_students()
    response = json_util.dumps(db_response)
    return Response(response, mimetype="application/json")
