from flask import Blueprint, request, jsonify
from bson import ObjectId
from app.users.models import UserModel

users_blueprint = Blueprint(
    name="users",
    import_name=__name__,
    url_prefix="/users"
)


@users_blueprint.route("/sign_in", methods=["POST"])
def hello_user():
    document = request.get_json()
    if not ("username" in document.keys()) or not ("password" in document.keys()) or not ("confirm_password" in document.keys()):
        return jsonify({"messagge": "Some argument is missing"}), 400

    if not (document["password"] == document["confirm_password"]):
        return jsonify({"messagge": "Passwords do not match"}), 400

    db_response = UserModel.create_user(document)
    if "__id" in db_response.keys():
        return (jsonify(db_response), 201)

    return (jsonify(db_response), 400)
