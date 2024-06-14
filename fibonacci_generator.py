# Program to Generator Fibonacci_Series to n Using Generator
from check_number_input import is_number


def fib_generator():
    n1, n2 = 0, 1
    while True:
        yield n1
        n1, n2 = n2, n1+n2
