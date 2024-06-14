# Generator Function to Find all the Number to Access Which are Divisible by 7
from check_number_input import is_number
from divisible_by_n import divisible


def divisible_generator(divisor):
    if is_number(divisor):
        i = 1
        while True:
            if divisible(divisor, i):
                yield i
            i += 1
    else:
        print("Enter a Number Input")

