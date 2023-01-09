import os


class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY")

    # flask-SQLAlchemy
    SQLALCHEMY_DATABASE_URI = "sqlite:///tasklist.db"
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
