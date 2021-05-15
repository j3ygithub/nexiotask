class DevelopmentConfig:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JSONIFY_PRETTYPRINT_REGULAR = True
    TESTING = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///sqlite.db"


class TestingConfig:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JSONIFY_PRETTYPRINT_REGULAR = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
