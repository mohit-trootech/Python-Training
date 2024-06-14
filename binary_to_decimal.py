# Program to Covert any binary number to decimal Number
import sys
from check_number_input import is_number


def binary2decimal(binary):
    decimal = 0
    size_binary = len(binary) - 1
    if is_number(binary):
        for i in binary:
            decimal += int(i) * (2 ** size_binary)
            size_binary -= 1
    return decimal


if __name__ == "__main__":
    try:
        print(f"Binary {sys.argv[1]} is equivalent to Decimal {binary2decimal(sys.argv[1])}")
    except:
        print(binary2decimal("1111"))
