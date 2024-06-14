# Python Recursion for find power of a**b
from check_number_input import is_number


def power(a, b):
    if is_number(str(a)) and is_number(str(b)):
        if a == 0:
            return 0
        elif b == 0:
            return 1
        elif b == 1:
            return a
        return a * power(a, b - 1)


if __name__ == "__main__":
    print(power(3,4))