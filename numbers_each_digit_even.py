# find all such numbers till 1000 such that each digit of the number is an even number.
from check_number_input import is_number


num = input("Enter the Number : ")
series = []


def is_digit_even(digits):
    for i in digits:
        if int(i) % 2 != 0:
            return False
    else:
        return True


if is_number(num):
    for i in range(int(num)+1):
        if is_digit_even(str(i)):
            series.append(i)
    print(series)
