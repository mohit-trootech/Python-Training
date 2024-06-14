# Python Program to Find Factorial of Given Number Using function Can be Used as Module
from check_number_input import is_number
from functools import reduce
from sys import argv


def factorial(num):
    if is_number(num):
        lst = list(range(1, num + 1))
        fact = reduce(lambda a, b: a * b, lst)
        return {"series": lst, "factorial": fact}


if __name__ == "__main__":
    try:
        print(factorial(argv[1]))
    except:
        print(factorial(5))
