import datetime
from decouple import config


username = config("username_from_db")
password = config("password_from_db")
database_name = config("database_name")


class Config():
    SECRET_KEY = config("secret_key")
    MONGO_URI = f"mongodb+srv://{username}:{password}@unet-db.rfzm9.mongodb.net/{database_name}?retryWrites=true&w=majority&ssl=true"
    JWT_SECRET_KEY = config("jwt_secret_key")


class Development(Config):
    ENV = "dev"
    DEBUG = True
    JWT_EXPIRATION_DELTA = datetime.timedelta(seconds=120)

class Production(Config):
    ENV = "prod"
    DEBUG = False
    JWT_EXPIRATION_DELTA = datetime.timedelta(seconds=60)


class Test(Config):
    pass
