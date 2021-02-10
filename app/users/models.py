from werkzeug.security import generate_password_hash, check_password_hash
from app.extensions import mongo


class UserModel():

    @classmethod
    def create_user(cls, data):

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
