from ..config_app import get_socketio

socketio = get_socketio()

def notifier(func):
    global socketio
    def wrapper(*args, **kwargs):
        socketio.emit("test_started", {"name_test": "Test1"})
        result = func(*args, **kwargs)
        return result
    return wrapper