from flask import Blueprint, abort, jsonify, request
from marshmallow.exceptions import ValidationError
from sqlalchemy.exc import IntegrityError

from core import status_codes
from core.utils import get_object_or_404
from models import User, UserSchema, db

user = Blueprint("user", __name__)


@user.route("/users", methods=["GET"])
def user_list():
    users = User.query.all()
    data = UserSchema(many=True).dump(users)
    return jsonify(data)


@user.route("/users", methods=["POST"])
def user_create():
    data = request.get_json()
    try:
        cleaned_data = UserSchema().load(data)
    except ValidationError:
        abort(status_codes.BAD_REQUEST)
    user = User(**cleaned_data)
    db.session.add(user)
    try:
        db.session.commit()
    except IntegrityError:
        abort(status_codes.BAD_REQUEST)
    return jsonify(cleaned_data), status_codes.CREATED


@user.route("/users/<int:pk>", methods=["GET"])
def user_retrieve(pk):
    user = get_object_or_404(model=User, pk=pk)
    data = UserSchema().dump(user)
    return jsonify(data), status_codes.OK


@user.route("/users/<int:pk>", methods=["PUT"])
def user_update(pk):
    user = User.query.get(pk)
    if not user:
        abort(status_codes.NOT_FOUND)
    data = request.get_json()
    try:
        cleaned_data = UserSchema().load(data)
    except ValidationError:
        abort(status_codes.BAD_REQUEST)
    for key, value in cleaned_data.items():
        setattr(user, key, value)
    try:
        db.session.commit()
    except IntegrityError:
        abort(status_codes.BAD_REQUEST)
    return jsonify(cleaned_data), status_codes.OK


@user.route("/users/<int:pk>", methods=["DELETE"])
def user_destroy(pk):
    user = User.query.get(pk)
    db.session.delete(user)
    try:
        db.session.commit()
    except IntegrityError:
        abort(status_codes.BAD_REQUEST)
    return jsonify(), status_codes.NO_CONTENT
