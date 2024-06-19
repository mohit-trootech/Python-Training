"""Sample Python File tp Check Time Complexity of Functions"""
from time import time, sleep


def check_complexity(fun):
    def inner(*args, **kwargs):
        before = time()
        results = fun(*args, **kwargs)
        after = time()
        print("Time Taken in {} Complexity: {:.9f}".format(fun.__name__, after-before))
        return results
    return inner


if __name__ == "__main__":
    @check_complexity
    def hello(msg: str) -> None:
        """
        Test Message to Print Hello World
        @param msg: str
        @return: None
        """
        return msg
    print(hello("print"))


