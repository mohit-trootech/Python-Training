# Module to Return Arithmetic Progression
from check_number_input import is_number


def arithmetic_progression(start, end, difference):
    if is_number(str(start)) and is_number(str(end)) and is_number(str(difference)):
        return [i for i in range(int(start), int(end)+1, int(difference))]


def geometric_progression(start, end, ratio):
    if is_number(str(start)) and is_number(str(end)) and is_number(str(ratio)):
        return [i*int(ratio) for i in range(int(start), int(end)+1)]

