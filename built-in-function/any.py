"""
Any - Anything: Return True if any element of the iterable is true. If the iterable is empty, return False
"""


def any_example(lst: list) -> bool:
    for element in lst:
        if element:
            return True
    else:
        return False


print(any_example([1+2j]))
