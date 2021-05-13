from flask import jsonify, request
from settings import app
from models import User
from schemas import UserSchema


@app.route("/")
def index():
    return {"msg": "hello world!"}


@app.route("/users", methods=["GET"])
def user_list():
    users = User.query.all()
    users_schema = UserSchema(many=True)
    data = users_schema.dump(users)
    return jsonify(data)


@app.route("/users/<int:id>", methods=["GET"])
def user_retrieve(id):
    user = User.query.get(id)
    user_schema = UserSchema()
    data = user_schema.dump(user)
    return jsonify(data)


@app.route("/users", methods=["POST"])
def user_create():
    user = {
        "name": request.values["name"],
        "job_title": request.values["job_title"],
    }
    user = User(user)
    status = 201
    return jsonify(user), status


# def get_resource(resources, pk, pk_field='id'):
#     for resource in resources:
#         if resource.get(pk_field) == pk:
#             return resource
#     abort(404)


# @app.route("/users/<int:id>", methods=["GET"])
# def user_retrieve(id):
#     user = get_resource(users, id)
#     return jsonify(user)


# @app.route("/users/<int:id>", methods=["PUT"])
# def user_update(id):
#     request_data = request.get_json()
#     user = get_resource(users, id)
#     user.update(request_data)
#     return jsonify(user)


# @app.route("/users/<int:id>", methods=["DELETE"])
# def user_destroy():
#     user = get_resource(users, id)
#     del user
#     return jsonify()
