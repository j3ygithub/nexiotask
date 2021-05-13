
from settings import db, ma


class User(db.Model):
    __tablename__ = 'usertable'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)


class UserSchema(ma.Schema):
    class Meta:
        model = User
        sqla_session = db.session
