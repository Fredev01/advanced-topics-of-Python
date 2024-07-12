from flask_socketio import SocketIO
from flask_cors import CORS
from flask import Flask, json, request, jsonify
from .apis import app_fixture_components, app_test_suite
import logging
logging.getLogger('werkzeug').setLevel(logging.ERROR)
logging.getLogger('flask.app').setLevel(logging.ERROR)


def get_app() -> tuple[SocketIO, Flask]:
    app = Flask(__name__)
    socketio = SocketIO(app, cors_allowed_origins="*")
    CORS(app, resources=r'/api/*', origins="*")
    app.register_blueprint(app_fixture_components)
    app.register_blueprint(app_test_suite)

    return socketio, app
