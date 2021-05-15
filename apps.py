from flask import Flask
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from configs import DevelopmentConfig, TestingConfig

db = SQLAlchemy()
ma = Marshmallow()


def create_app(app_name):
    """
    Application factories
    https://flask.palletsprojects.com/en/2.0.x/patterns/appfactories/
    """
    configs = {
        "development": DevelopmentConfig,
        "testing": TestingConfig,
    }
    try:
        config = configs[app_name]
    except KeyError:
        raise ValueError(f'"{app_name}" is not a valid app_name.')
    app = Flask(__name__)
    app.config.from_object(config)
    db.init_app(app)
    ma.init_app(app)

    from core.views import core

    app.register_blueprint(core)

    from user.views import user

    app.register_blueprint(user)

    return app
