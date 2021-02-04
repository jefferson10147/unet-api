from decouple import config


class Config():
    SECRET_KEY = config("secret_key")


class Development(Config):
    ENV = "dev"
    DEBUG = True


class Production(config):
    ENV = "prod"


class Test(config):
    pass
