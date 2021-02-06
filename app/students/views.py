from bson import json_util, ObjectId
from flask import Blueprint, Response

from .models import StudentsModel


students_blueprint = Blueprint(
    name="students",
    import_name=__name__,
    url_prefix="/api/students"
)
students_model = StudentsModel()


@students_blueprint.route('/')
def all_students():
    db_response = students_model.get_all_students()
    return Response(json_util.dumps(db_response), mimetype="application/json")


@students_blueprint.route("/id/<id>")
def student_by_id(id):
    db_response = students_model.get_student_by_id(ObjectId(id))
    return Response(json_util.dumps(db_response), mimetype="application/json")
