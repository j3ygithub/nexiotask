from flask import Blueprint, jsonify, request

from core import status_codes
from core.shortcuts import get_cleaned_data_or_400, get_object_or_404

from .models import User, UserSchema, db

user = Blueprint("user", __name__)


@user.route("/users", methods=["GET"])
def user_list():
    users = User.query.all()
    data = UserSchema(many=True).dump(users)
    return jsonify(data), status_codes.OK


@user.route("/users", methods=["POST"])
def user_create():
    data = request.get_json()
    cleaned_data = get_cleaned_data_or_400(data, schema_class=UserSchema)
    user = User(**cleaned_data)
    user.create(db_session=db.session)
    return jsonify(cleaned_data), status_codes.CREATED


@user.route("/users/<int:pk>", methods=["GET"])
def user_retrieve(pk):
    user = get_object_or_404(model=User, pk=pk)
    data = UserSchema().dump(user)
    return jsonify(data), status_codes.OK


@user.route("/users/<int:pk>", methods=["PUT"])
def user_update(pk):
    user = get_object_or_404(model=User, pk=pk)
    data = request.get_json()
    cleaned_data = get_cleaned_data_or_400(data, schema_class=UserSchema)
    user.update(cleaned_data, db_session=db.session)
    return jsonify(cleaned_data), status_codes.OK


@user.route("/users/<int:pk>", methods=["DELETE"])
def user_destroy(pk):
    user = get_object_or_404(model=User, pk=pk)
    user.delete(db_session=db.session)
    return jsonify(), status_codes.NO_CONTENT
