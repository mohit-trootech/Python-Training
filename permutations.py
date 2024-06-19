"""Python Module to Find Permutation nPr Formar"""
import math


def permutation(n: int, r: int) -> int:
    """
    to calculate permutation based on nPr Implementation
    @param n: int
    @param r: int
    @return: int
    """
    return math.factorial(n)/math.factorial(n - r)


if __name__ == "__main__":
    print(permutation(5,4))





