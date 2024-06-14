# Get Even Number list Till n
from check_number_input import is_number


def is_even(num):
    is_number(str(num))
    if int(num)%2 == 0:
        return True
    else:
        return False

