from models.actions import Actions
from models.fixture_component import FixtureComponent
from models.status import Status
from datetime import datetime


class Relay(FixtureComponent):

    def __init__(self, id: int, name: str, label_energize: str = "Energizar", label_de_energize: str = "De-energize", options: list = []):
        super().__init__(id,name, type="Relay")
        self.energize = Actions(self.energize, None, name=label_energize)
        self.de_energize = Actions(self.de_energize, None, name=label_de_energize)
        self.status = Status("Estado","# de operaciones", options=options)
        self.init()

    def energize(self, *args):
        print(f"energizando relevador {self.id}")
        now = datetime.now()
        time_stamp_formated = now.strftime("%d-%B-%Y %H:%M:%S")
        self.logs.append(f"{time_stamp_formated} Energizando relevador {self.id}")
        return self.logs

    def de_energize(self):
        print(f"energizando relevador {self.id}")
        now = datetime.now()
        time_stamp_formated = now.strftime("%d-%B-%Y %H:%M:%S")
        self.logs.append(f"{time_stamp_formated} Des-Energizando relevador {self.id}")
        return self.logs
