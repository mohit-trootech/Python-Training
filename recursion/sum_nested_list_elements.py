# Program to find sum of nested list elements
import sys


def sum_nested_list(lst):
    s = 0
    for elements in lst:
        if type(elements) == type([]):
            return s + sum_nested_list(elements)
        else:
            s += elements
    return s


if __name__ == "__main__":
    try:
        print(sum_nested_list(sys.argv[1]))
    except:
        print(sum_nested_list([1]))