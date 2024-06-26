"""
Generator Function are used to generate a iterable object which yield value till StopIteration Error
"""


def fib_generator():
    n1, n2 = 0, 1
    while True:
        yield n1
        n1, n2 = n2, n1 + n2


if __name__ == "__main__":
    sequence = fib_generator()
    s = {i: next(sequence) for i in range(1, 10)}
    print(s)
