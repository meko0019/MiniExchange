import os

DATABASE_URL = os.environ.get("DATABASE_URL", "postgresql://localhost:5432/postgres")

class BaseConfig(object):
    HOST = "127.0.0.1"
    PORT = 5000

    SQLALCHEMY_DATABASE_URI = DATABASE_URL
    SQLALCHEMY_TRACK_MODIFICATIONS = False



class DevelopmentConfig(BaseConfig):
    DEBUG = True
    TESTING = True

    SECRET_KEY = "not-a-secret-key"


class ProductionConfig(BaseConfig):
    DEBUG = False
    TESTING = False

    SECRET_KEY = os.environ.get("SECRET_KEY", None)
