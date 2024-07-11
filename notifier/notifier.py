from types import MethodType
# from abc import ABCMeta
import requests
from requests.exceptions import HTTPError, Timeout


class ClientHttp:
    _instance = None
    _count_instance = 0

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._count_instance += 1
        return cls._instance

    def __init__(self, base_url: str, ):
        self.base_url = base_url

    def __repr__(self):
        return f"ClientHttp: base_url={self.base_url}"

    def post(self, endpoint: str, payload: dict, headers: dict = {'Content-Type': 'application/json'}):
        try:
            response = requests.post(f"{self.base_url}{endpoint}", json=payload, headers=headers, timeout=0.3)
            response.raise_for_status()
            print("Success:", response.json())
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')
        except Timeout as timeout_err:
            print(f'Timeout error occurred: {timeout_err}')
        except Exception as err:
            print(f'Other error occurred: {err}')

    @classmethod
    def get_count_instance(cls):
        return cls._count_instance


class WebSocket:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance
    def __init__(self):
        pass



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
        print(f"After executing function {self.func.__name__}: {result}")
        return result

    def __get__(self, instance, owner):
        return self if instance is None else MethodType(self, instance)

    @classmethod
    def get_count_instance(cls):
        return cls._count_instance


def notifier(func):
    client_http = ClientHttp("http://192.168.168.101:8080")

    def wrapper(*args, **kwargs):
        client_http.post("/api/test_started", {"name_test": "Test1"})
        result = func(*args, **kwargs)
        return result
    return wrapper


