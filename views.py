from flask import jsonify, request
from settings import db, app
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


@app.route("/users", methods=["POST"])
def user_create():
    user = User(**request.values)
    db.session.add(user)
    db.session.commit()
    user_schema = UserSchema()
    data = user_schema.dump(request.values)
    return jsonify(data), 201


@app.route("/users/<int:id>", methods=["GET"])
def user_retrieve(id):
    user = User.query.get(id)
    user_schema = UserSchema()
    data = user_schema.dump(user)
    return jsonify(data)


@app.route("/users/<int:id>", methods=["PUT"])
def user_update(id):
    user = User.query.get(id)
    db.session.delete(user)
    db.session.commit(user)
    return jsonify(), 204


@app.route("/users/<int:id>", methods=["DELETE"])
def user_destroy():
    user = User.query.get(id)
    db.session.delete(user)
    db.session.commit(user)
    return jsonify()
