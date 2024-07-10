import logging

class Actions:

    def __init__(self, run, *args, name: str = "Execute"):
        self.run = run
        self.args = args
        self.name = name

    def run(self):
        logging.debug("Executing run")
        self.run(self.args)

    def get_render_metadata(self):
        return {
            "label": self.name
        }





