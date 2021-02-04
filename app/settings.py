from decouple import config


class Config():
    SECRET_KEY = config("secret_key")


class Development(Config):
    ENV = "dev"
    DEBUG = True
