from flask import Blueprint, Response, jsonify, request
from bson import json_util, ObjectId
from flask_jwt_extended import jwt_required

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


@students_blueprint.route("/search/students/name/<string:name>/lastname/<string:lastname>")
def students_by_name_and_lastname(name, lastname):
    db_response = students_model.get_students_by_name_and_lastname(
        name, lastname)
    return Response(json_util.dumps(db_response), mimetype="application/json")


@students_blueprint.route("/search/students/career/<string:career>")
def students_by_career(career):
    db_response = students_model.get_students_by_career(career)
    return Response(json_util.dumps(db_response), mimetype="application/json")


@students_blueprint.route("/search/student/id/<string:id>")
def student_by_id(id):
    db_response = students_model.get_student_by_id(ObjectId(id))
    return Response(json_util.dumps(db_response), mimetype="application/json")


@students_blueprint.route("/search/student/dni/<string:dni>")
def student_by_dni(dni):
    db_response = students_model.get_student_by_dni(''.join(['V', dni]))
    return Response(json_util.dumps(db_response), mimetype="application/json")


@students_blueprint.route("/insert", methods=["POST"])
@jwt_required
def insert_student():
    document = request.get_json()
    db_response = students_model.insert_one_student(document)
    return (jsonify({"__id": str(db_response)}), 201)


@students_blueprint.route("/insert_many", methods=["POST"])
@jwt_required
def insert_students():
    documents = request.get_json()
    db_response = students_model.insert_students(documents)
    return (jsonify(db_response), 201)


@students_blueprint.route("/update", methods=["PUT"])
@jwt_required
def update_student():
    document = request.get_json()
    db_response = students_model.update_student_by_dni(document)
    return (jsonify({"modified_count": str(db_response)}))


@students_blueprint.route("/delete/<string:dni>", methods=["DELETE"])
@jwt_required
def delete_student(dni):
    db_response = students_model.delete_student_by_dni(dni)
    return Response(json_util.dumps(db_response), mimetype="application/json")


@students_blueprint.app_errorhandler(404)
def not_found(error=None):
    message = {
        "message": "This resource was not found",
        "status": 404
    }
    response = jsonify(message)
    response.status_code = 404
    return response
