from abc import ABC, abstractmethod
from notifier.notifier import Notifier


class Test(ABC):
    @abstractmethod
    def execute(self, fixture):
        pass


class Test1(Test):
    def __init__(self, data):
        self.data = data

    @Notifier
    def execute(self, fixture):
        print("inside the function execute")
        return f"Hello from Test1 {fixture} "
