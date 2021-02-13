import datetime
from decouple import config


username = config("username_from_db")
password = config("password_from_db")
database_name = config("database_name")
admin_key = config("admin_key")


class Config():
    SECRET_KEY = config("secret_key")
    MONGO_URI = f"mongodb+srv://{username}:{password}@unet-db.rfzm9.mongodb.net/{database_name}?retryWrites=true&w=majority&ssl=true"
    JWT_SECRET_KEY = config("jwt_secret_key")
    JWT_ACCESS_TOKEN_EXPIRES = datetime.timedelta(seconds=60)


class Development(Config):
    ENV = "dev"
    DEBUG = True


class Production(Config):
    ENV = "prod"
    DEBUG = False


class Test(Config):
    pass
