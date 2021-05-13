from flask import abort, make_response

from models import User
from schemas import UserSchema
from settings import db


def read_all():
    users = User.query.order_by(User.lname).all()

    user_schema = UserSchema(many=True)
    data = user_schema.dump(users)
    return data


def read_one(user_id):
    user = User.query.filter(User.user_id == user_id).one_or_none()

    if user is not None:

        user_schema = UserSchema()
        data = user_schema.dump(user)
        return data

    else:
        abort(
            404,
            "User not found for Id: {user_id}".format(user_id=user_id),
        )


def create(user):
    fname = user.get("fname")
    lname = user.get("lname")

    existing_user = (
        User.query.filter(User.fname == fname)
        .filter(User.lname == lname)
        .one_or_none()
    )

    if existing_user is None:

        schema = UserSchema()
        new_user = schema.load(user, session=db.session)

        db.session.add(new_user)
        db.session.commit()

        data = schema.dump(new_user)

        return data, 201

    else:
        abort(
            409,
            "User {fname} {lname} exists already".format(
                fname=fname, lname=lname
            ),
        )


def update(user_id, user):
    update_user = User.query.filter(
        User.user_id == user_id
    ).one_or_none()

    fname = user.get("fname")
    lname = user.get("lname")

    existing_user = (
        User.query.filter(User.fname == fname)
        .filter(User.lname == lname)
        .one_or_none()
    )

    if update_user is None:
        abort(
            404,
            "User not found for Id: {user_id}".format(user_id=user_id),
        )

    elif (
        existing_user is not None and existing_user.user_id != user_id
    ):
        abort(
            409,
            "User {fname} {lname} exists already".format(
                fname=fname, lname=lname
            ),
        )

    else:

        schema = UserSchema()
        update = schema.load(user, session=db.session)

        update.user_id = update_user.user_id

        db.session.merge(update)
        db.session.commit()

        data = schema.dump(update_user)

        return data, 200


def delete(user_id):
    user = User.query.filter(User.user_id == user_id).one_or_none()

    if user is not None:
        db.session.delete(user)
        db.session.commit()
        return make_response(
            "User {user_id} deleted".format(user_id=user_id), 200
        )

    else:
        abort(
            404,
            "User not found for Id: {user_id}".format(user_id=user_id),
        )
