from models.actions import Actions
from models.status import Status
import logging


class FixtureComponent:
    def __init__(self, id: int, name, type: str):

        self.id = id
        self.name = name
        self.type = type
        self.actions: list[Actions] = list()
        self.statuses: list[Status] = list()
        self.logs = list()

    def init(self):

        for key, item in self.__dict__.items():
            if isinstance(item, Actions):
                logging.debug("agregando item a actions")
                self.actions.append(item)
            elif isinstance(item,Status):
                logging.debug("agregando item a statuses")
                self.statuses.append(item)



if __name__ == "__main__":
    test = FixtureComponent(1, "jsjs", "relay")

    test.init()