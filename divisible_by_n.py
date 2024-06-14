# Program to Check if Number is Divisible by n
from check_number_input import is_number


def divisible(number, divisor):
    if is_number(number):
        if int(number) % int(divisor) == 0:
            return True
        else:
            return False
    else:
        print("Not a Number")

