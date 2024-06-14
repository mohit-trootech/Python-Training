"""Python Program to Find Sum to N using Recursion"""
import sys


def sum_2_n(num):
    if num == 1:
        return 1
    return num + sum_2_n(num - 1)


if __name__ == "__main__":
    print(sum_2_n(5))
