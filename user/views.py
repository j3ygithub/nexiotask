from flask import Blueprint, abort, jsonify, request
from marshmallow.exceptions import ValidationError
from sqlalchemy.exc import IntegrityError
from models import User, UserSchema, db

user = Blueprint("user", __name__)


@user.route("/users", methods=["GET"])
def user_list():
    users = User.query.all()
    users_schema = UserSchema(many=True)
    data = users_schema.dump(users)
    return jsonify(data)


@user.route("/users", methods=["POST"])
def user_create():
    data = request.get_json()
    try:
        cleaned_data = UserSchema().load(data)
    except ValidationError:
        abort(500)
    user = User(**cleaned_data)
    db.session.add(user)
    try:
        db.session.commit()
    except IntegrityError:
        abort(500)
    return jsonify(cleaned_data), 201


@user.route("/users/<int:pk>", methods=["GET"])
def user_retrieve(pk):
    user = User.query.get(pk)
    if not user:
        abort(404)
    user_schema = UserSchema()
    data = user_schema.dump(user)
    return jsonify(data)


@user.route("/users/<int:pk>", methods=["PUT"])
def user_update(pk):
    user = User.query.get(pk)
    if not user:
        abort(404)
    db.session.delete(user)
    db.session.commit()
    return jsonify(), 200


@user.route("/users/<int:pk>", methods=["DELETE"])
def user_destroy(pk):
    user = User.query.get(pk)
    if not user:
        abort(404)
    db.session.delete(user)
    db.session.commit()
    return jsonify(), 204
