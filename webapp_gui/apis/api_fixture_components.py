from flask import Blueprint, Response, jsonify, request


app = Blueprint('fixtureComponent', __name__, url_prefix='/api/fixture_components')


@app.get("/greeting")
def greet():
    return jsonify({'msg': "hello from api fixtureComponent "}), 200
