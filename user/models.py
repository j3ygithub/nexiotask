from app import db, ma
from core.models import SQLAlchemyActionMixin


class User(db.Model, SQLAlchemyActionMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(63), nullable=False, unique=True)
    job_title = db.Column(db.String(63), nullable=False)
    communicate_information = db.Column(db.String(255), nullable=False)


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
