import datetime
import os

username = os.getenv("username_from_db")
password = os.getenv("password_from_db")
database_name = os.getenv("database_name")
admin_key = os.getenv("admin_key")


class Config:
    SECRET_KEY = os.getenv("secret_key")
    MONGO_URI = f"mongodb+srv://{username}:{password}@unet-db.rfzm9.mongodb.net/{database_name}?retryWrites=true&w=majority&ssl=true"
    JWT_SECRET_KEY = os.getenv("jwt_secret_key")
    JWT_ACCESS_TOKEN_EXPIRES = datetime.timedelta(seconds=60)


class Development(Config):
    ENV = "dev"
    DEBUG = True


class Production(Config):
    ENV = "prod"
    DEBUG = False


class Test(Config):
    pass
