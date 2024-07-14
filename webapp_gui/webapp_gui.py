import time

from .config_app import get_app
from threading import Thread, Event
from multiprocessing import Process
import sys


class WebAppGUI:

    def __init__(self, test_suite):
        self.test_suite = test_suite
        self.thread_app = None

    def _run_app(self, port: str = "8080"):
        socketio, app = get_app()
        try:
            socketio.run(app=app, host="0.0.0.0", allow_unsafe_werkzeug=True, port=port)
        except KeyboardInterrupt:
            print(f"bye from WebAppGUI ;)")
            time.sleep(1)
            sys.exit()
        except Exception as e:
            print(e)
            time.sleep(1)
            sys.exit()


    def start(self, port: str = "8080"):
        self.thread_app = Thread(target=self._run_app, name="webAppGUI", args=(port,))
        self.thread_app.daemon = True
        self.thread_app.start()

    def stop(self):
        if self.thread_app is not None:
            time.sleep(1)
            sys.exit()

