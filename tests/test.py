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


def main():
    list_test_suite = [{'name': "Test1", 'criteria': {'expected_value': '2'}},
                       {'name': "Test2", 'criteria': {'expected_value': '4'}},
                       {'name': "Test3", 'criteria': {'expected_value': '6'}}]
    test_suite_result = [{'name': "Test1", 'criteria': {'expected_value': '2'}, 'success': True, 'data': '2'},
                         ]
    len_test_suite_result = len(test_suite_result)
    if len_test_suite_result > 0:
        new_test_suite = [
            test_suite_result[index] if index < len(test_suite_result) and test['name'] == test_suite_result[index][
                'name']
            else test
            for index, test in enumerate(list_test_suite)
        ]
        return new_test_suite
    return list_test_suite

if __name__ == "__main__":
    result = main()
    print(result)
    print(len(result))