from decouple import config


username = config("username_from_db")
password = config("password_from_db")
database_name = config("database_name")


class Config():
    SECRET_KEY = config("secret_key")
    MONGO_URI = f"mongodb+srv://{username}:{password}@unet-db.rfzm9.mongodb.net/{database_name}?retryWrites=true&w=majority&ssl=true"


class Development(Config):
    ENV = "dev"
    DEBUG = True


class Production(Config):
    ENV = "prod"
    DEBUG = False


class Test(Config):
    pass
