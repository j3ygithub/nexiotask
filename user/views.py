from flask import Blueprint, abort, jsonify, request

from models import User, UserSchema, db
from marshmallow.exceptions import ValidationError

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
    db.session.commit()
    return jsonify(cleaned_data), 201


@user.route("/users/<int:id>", methods=["GET"])
def user_retrieve(id):
    user = User.query.get(id)
    if not user:
        abort(404)
    user_schema = UserSchema()
    data = user_schema.dump(user)
    return jsonify(data)


@user.route("/users/<int:id>", methods=["PUT"])
def user_update(id):
    user = User.query.get(id)
    if not user:
        abort(404)
    db.session.delete(user)
    db.session.commit()
    return jsonify(), 200


@user.route("/users/<int:id>", methods=["DELETE"])
def user_destroy(id):
    user = User.query.get(id)
    if not user:
        abort(404)
    db.session.delete(user)
    db.session.commit()
    return jsonify(), 204
