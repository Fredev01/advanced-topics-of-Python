# config.py

from flask_socketio import SocketIO
from flask import Flask

app = Flask(__name__)
socketio = SocketIO(app)


