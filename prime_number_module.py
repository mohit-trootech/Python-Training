# Python Program to Find Prime Number
from sys import argv


def is_prime(num):
    num = str(num)
    if num.isnumeric():
        num = int(num)
    else:
        return "Enter Valid Integer Input"

    for i in range(2, num):
        if num == 1:
            print(f"{num} is Not Prime nor Composite")
            return False

        elif num == 2 or num == 3:
            return True
        elif num % i == 0:
            return False
    else:
        return True


if __name__ == "__main__":
    try:
        print(is_prime(argv[1]))
    except:
        print(is_prime(7))
