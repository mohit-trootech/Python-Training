# Python program to Create a Module for Sample Dictionary
from check_number_input import is_number
from integer_2_roman import integer_2_roman_numeral
from progression_module import arithmetic_progression, geometric_progression


def arithmetic_progression_dictionary(start, end, difference):
    if is_number(str(start)) and is_number(str(end)) and is_number(str(difference)):
        ap_dict = {"series": arithmetic_progression(start, end, difference)}
        ap_dict["sum"] = sum(ap_dict.get("series"))
        return ap_dict


def geometric_progression_dictionary(start, end, ratio):
    if is_number(str(start)) and is_number(str(end)) and is_number(str(ratio)):
        gp_dict = {"series": geometric_progression(start, end, ratio)}
        gp_dict["sum"] = sum(gp_dict.get("series"))
        return gp_dict


def square_2_n_dictionary(n):
    if is_number(str(n)):
        return {i: i ** 2 for i in range(1, int(n) + 1)}


def cube_2_n_dictionary(n):
    if is_number(str(n)):
        return {i: i ** 3 for i in range(1, int(n) + 1)}


def roman_2_n(length):
    if is_number(str(length)):
        return {i: integer_2_roman_numeral(i) for i in range(length + 1)}
