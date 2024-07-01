"""Sample Python File tp Check Time Complexity of Functions"""

from time import time, sleep
from functools import wraps


def check_complexity(fun):
    """
    Check Time Complexity
    """

    @wraps(fun)
    def inner(*args, **kwargs):
        """
        Wrapper Time Complexity
        """
        before = time()
        result = fun(*args, **kwargs)
        after = time()
        print(
            "Time Taken in {} Complexity: {:.9f}".format(fun.__name__, after - before)
        )
        if result:
            return result

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

    a = hello("Hii")
    print(a)

    print(check_complexity.__doc__)
