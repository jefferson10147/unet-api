from werkzeug.security import generate_password_hash, check_password_hash

from app.extensions import mongo
from app.settings import admin_key


class UserModel():

    def __init__(self, username):
        self.username = username

    @classmethod
    def create_user(cls, data):
        if data["admin_key"] != admin_key:
            return {"Message": "Sorry, auth_key to create an user isn't valid."}

        if cls.check_if_user_exits(data["username"]):
            return {"Message": "Username already exists."}

        response = mongo.db.users.insert_one({
            "username": data["username"],
            "password": generate_password_hash(data["password"])
        })

        return {"__id": str(response.inserted_id)}

    @classmethod
    def check_if_user_exits(cls, username):
        count = mongo.db.users.find({"username": username}).count()
        if count:
            return True

    @classmethod
    def get_user(cls, data):
        user = mongo.db.users.find_one({"username": data["username"]})
        if user and check_password_hash(user["password"], data["password"]):
            return UserModel(user["username"])
