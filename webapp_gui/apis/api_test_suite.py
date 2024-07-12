from flask import Blueprint, Response, jsonify, request


app = Blueprint(name='TestSuites',import_name= __name__, url_prefix='/api/test_suites')


@app.get("/greeting")
def greet():
    return jsonify({'msg': "hello from api TestSuite "}), 200

