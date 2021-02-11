import datetime
from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from bson import ObjectId

from app.users.models import UserModel


users_blueprint = Blueprint(
    name="users",
    import_name=__name__,
    url_prefix="/users"
)


@users_blueprint.route("/sign_in", methods=["POST"])
def sign_in():
    json_args = request.get_json()
    if not json_args:
        return jsonify({"messagge": "Missing Json in body request"}), 400

    if not("auth_key" in json_args.keys()):
        return jsonify({"messagge": "You need an auth_key to create an user."}), 400

    if not ("username" in json_args.keys()) or not ("password" in json_args.keys()) or not ("confirm_password" in json_args.keys()):
        return jsonify({"messagge": "Some argument is missing"}), 400

    if not (json_args["password"] == json_args["confirm_password"]):
        return jsonify({"messagge": "Passwords do not match"}), 400

    db_response = UserModel.create_user(json_args)
    if "__id" in db_response.keys():
        return (jsonify(db_response), 201)

    return (jsonify(db_response), 400)


@users_blueprint.route("/login", methods=["POST"])
def login():
    json_args = request.get_json()
    if not json_args:
        return jsonify({"messagge": "Missing Json in body request"}), 400

    if not ("username" in json_args.keys()) or not ("password" in json_args.keys()):
        return jsonify({"messagge": "Some argument is missing"}), 400

    user = UserModel.get_user(json_args)
    if user:
        token = create_access_token(identity={"username": user.username})
        return jsonify({"acess_token": token}), 200

    return jsonify({"messagge": "Failed to authenticate"}), 400
