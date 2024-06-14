# Python Program to Check Number Import Module
from sys import argv


def is_number(num):
    num = str(num)
    if num.isdigit():
        return True
    else:
        print("Not a Integer Number Input")


if __name__ == "__main__":
    try:
        print(is_number(argv[1]))
    except:
        print(is_number("5"))
