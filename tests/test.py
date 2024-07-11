import time
from abc import ABC, abstractmethod
from notifier.notifier import notifier


class Test(ABC):
    @abstractmethod
    def execute(self, fixture):
        pass


class Test1(Test):
    def __init__(self, data):
        self.data = data

    @notifier
    def execute(self, fixture):
        print("inside the function execute")
        time.sleep(1)
        return f"Hello from Test1 {fixture} "
