class Status:
    def __init__(self, *args, options: list= ["Energizado", "Des-energizado"]):
        self.name = args
        self.options = options

    def get_render_metadata(self):

        return {
            "name": [arg for arg in self.name],
            "options": self.options
        }



