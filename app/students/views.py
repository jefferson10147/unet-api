from bson import json_util, ObjectId
from flask import Blueprint, Response

from .models import StudentsModel


students_blueprint = Blueprint(
    name="students",
    import_name=__name__,
    url_prefix="/api/v1"
)
students_model = StudentsModel()


@students_blueprint.route("/search/<string:expression>")
def search_by_expression(expression):
    db_response = students_model.get_students_by_expression(expression)
    return Response(json_util.dumps(db_response), mimetype="application/json")


@students_blueprint.route("/search/students")
def all_students():
    db_response = students_model.get_all_students()
    return Response(json_util.dumps(db_response), mimetype="application/json")


@students_blueprint.route("/search/students/name/<string:name>")
def students_by_name(name):
    db_response = students_model.get_students_by_name(name)
    return Response(json_util.dumps(db_response), mimetype="application/json")


@students_blueprint.route("/search/students/second_name/<string:second_name>")
def students_by_second_name(second_name):
    db_response = students_model.get_students_by_second_name(second_name)
    return Response(json_util.dumps(db_response), mimetype="application/json")


@students_blueprint.route("/search/students/lastname/<string:lastname>")
def students_by_lastname(lastname):
    db_response = students_model.get_students_by_lastname(lastname)
    return Response(json_util.dumps(db_response), mimetype="application/json")


@students_blueprint.route("/search/students/second_lastname/<string:second_lastname>")
def students_by_second_lastname(second_lastname):
    db_response = students_model.get_students_by_second_lastname(
        second_lastname
    )
    return Response(json_util.dumps(db_response), mimetype="application/json")


@students_blueprint.route("/search/student/id/<string:id>")
def student_by_id(id):
    db_response = students_model.get_student_by_id(ObjectId(id))
    return Response(json_util.dumps(db_response), mimetype="application/json")


@students_blueprint.route("/search/student/dni/<string:dni>")
def student_by_dni(dni):
    db_response = students_model.get_student_by_dni(''.join(['V', dni]))
    return Response(json_util.dumps(db_response), mimetype="application/json")
