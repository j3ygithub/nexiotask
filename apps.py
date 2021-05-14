from flask import Flask
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
ma = Marshmallow()


class DevelopmentConfig:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JSONIFY_PRETTYPRINT_REGULAR = True
    TESTING = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///sqlite.db"


class TestingConfig:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JSONIFY_PRETTYPRINT_REGULAR = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///sqlite-test.db"


def create_app(app_name):
    """
    Application factories
    https://flask.palletsprojects.com/en/2.0.x/patterns/appfactories/
    """
    app = Flask(__name__)
    if app_name == "development":
        from_object = DevelopmentConfig
        app.config.from_object(from_object)
    elif app_name == "testing":
        from_object = TestingConfig
        app.config.from_object(from_object)
    else:
        raise ValueError(f'"{app_name}" is not a valid app_name.')
    db.init_app(app)
    ma.init_app(app)
    return app
