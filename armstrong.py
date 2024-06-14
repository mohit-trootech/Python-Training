# Python Program to Check String is Armstrong
import sys

from check_number_input import is_number


def is_armstrong(num):
    if is_number(str(num)):
        s = 0
        for i in num:
            s += int(i)**len(num)
        if str(s) == str(num):
            return True
        else:
            return False


if __name__ == "__main__":
    try:
        print(is_armstrong(sys.argv[1]))
    except:
        print(is_armstrong("15"))
