from .config_app import get_app
from threading import Thread, Event
from multiprocessing import Process
class WebAppGUI:

    def __init__(self, test_suite):
        self.test_suite = test_suite
        self.process_app: Process | None = None
        # self.stop_event: Event = Event()

    def _run_app(self, port: str = "8080"):
        socketio, app = get_app()
        try:
            socketio.run(app=app, host="0.0.0.0", allow_unsafe_werkzeug=True, port=port)
        except KeyboardInterrupt:
            print(f"bye from WebAppGUI ;)")


    def start(self, port: str = "8080"):
        self.process_app = Process(target=self._run_app, name="webAppGUI", args=(port,))
        self.process_app.start()

    def stop(self):
        if self.process_app is not None:
            self.process_app.terminate()

