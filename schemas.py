from models import User
from settings import ma


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
