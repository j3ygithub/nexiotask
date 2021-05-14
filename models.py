from apps import db, ma


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(63))
    job_title = db.Column(db.String(63))
    communicate_information = db.Column(db.String(255))


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
