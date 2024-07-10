from types import MethodType
# from abc import ABCMeta


class Notifier(object):
    _instance = None
    _count_instance = 0

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._count_instance += 1
        return cls._instance

    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("Before executing function")
        result = self.func(*args, **kwargs)
        print(f"After executing function: {result}")
        return result

    def __get__(self, instance, owner):
        return self if instance is None else MethodType(self, instance)

    @classmethod
    def get_count_instance(cls):
        return cls._count_instance


