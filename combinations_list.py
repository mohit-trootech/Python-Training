"""Python program to Generate List Combinations"""
import itertools
from time_complexity import check_complexity


@check_complexity
def list_combination(lst: list) -> set:
    temp = []
    for i in lst:
        temp.extend(list(itertools.combinations(lst, i)))
    return set(temp)


if __name__ == "__main__":
    print(list_combination([1, 2, 153, 13, 61, 613, 163, 53]))
