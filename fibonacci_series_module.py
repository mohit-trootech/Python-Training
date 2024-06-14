# Python Program for Fibonacci Series - Please Enter Number Input
from sys import argv


def fibonacci_sequence(size):
    size = str(size)
    lst = [0, 1]
    if size.isnumeric():
        size = int(size)
    else:
        return "Enter a Integer Number Input"

    for i in range(size - 2):
        lst.append(lst[-1] + lst[-2])

    return f"Fibonacci Series - {lst}"


if __name__ == "__main__":
    print(fibonacci_sequence(argv[1]))
