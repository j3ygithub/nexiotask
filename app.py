from flask import Flask, abort, jsonify, request
from flask import Response
import json


app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

users = [
    {
        "id": 1,
        "name": "Charles",
        "job_title": "SRE",
    },
    {
        "id": 2,
        "name": "Allen",
        "job_title": "SRE",
    },
    {
        "id": 3,
        "name": "Jason",
        "job_title": "Backend Engineer",
    },
]


@app.route("/users", methods=["GET"])
def user_list():
    return jsonify({"users": users})


@app.route("/users", methods=["POST"])
def user_create():
    user = {
        "name": request.values["name"],
        "job_title": request.values["job_title"],
    }
    users.append(user)
    response = json.dumps(users, indent=4)
    return Response(response, status=201, mimetype='application/json')


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
