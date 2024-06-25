# Python Program to convert Integer Value to Roman
import sys
import constant
from check_number_input import is_number


symbols = constant.ROMAN_CONSTANTS


def integer_2_roman_numeral(num):
    if is_number(str(num)):
        num = int(num)
        roman_numeral = ""
        while True:
            for i, j in symbols.items():
                if i <= int(num):
                    roman_numeral = roman_numeral + j
                    num -= i
                    break
            if num == 0:
                break

        return roman_numeral


if __name__ == "__main__":
    try:
        print(integer_2_roman_numeral(sys.argv[1]))
    except:
        print(integer_2_roman_numeral("555"))
