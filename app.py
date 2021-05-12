from flask import Flask, abort, jsonify, request
from flask_sqlalchemy import SQLAlchemy

# Configs
app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sqlite.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)


# Views
@app.route("/users", methods=["GET"])
def user_list():
    users = User.query.all()
    return jsonify(users)


@app.route("/users", methods=["POST"])
def user_create():
    user = {
        "name": request.values["name"],
        "job_title": request.values["job_title"],
    }
    users.append(user)
    status = 201
    return jsonify(user), status


def get_resource(resources, pk, pk_field='id'):
    for resource in resources:
        if resource.get(pk_field) == pk:
            return resource
    abort(404)


@app.route("/users/<int:id>", methods=["GET"])
def user_retrieve(id):
    user = get_resource(users, id)
    return jsonify(user)


@app.route("/users/<int:id>", methods=["PUT"])
def user_update(id):
    request_data = request.get_json()
    user = get_resource(users, id)
    user.update(request_data)
    return jsonify(user)


@app.route("/users/<int:id>", methods=["DELETE"])
def user_destroy():
    user = get_resource(users, id)
    del user
    return jsonify()


if __name__ == "__main__":
    app.run(debug=True)
