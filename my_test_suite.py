from tests.test import Test1
from notifier.notifier import ClientHttp

def main():
    test1 = Test1({"data": ["jaj"]})
    for _ in range(10):
        result = test1.execute("some Fixture")
        print(f"end result {result}")

    print(ClientHttp.get_count_instance())


if __name__ == "__main__":
    main()
