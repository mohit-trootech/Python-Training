# Temporary Program to Check Shell Argument
import sys


def temporary(num):
    print(f"You Entered {num} Type = {type(num)}")


if __name__ == "__main__":
    temporary(sys.argv[1])
