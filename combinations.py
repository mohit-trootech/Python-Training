"""Python Module to Find Combination nCr Format"""
import math
from time_complexity import check_complexity


@check_complexity
def combination(n: int, r: int) -> int:
    """
    to calculate Combination based on nCr Implementation
    @param n: int
    @param r: int
    @return: int
    """
    return math.factorial(n) / (math.factorial(n - r) * math.factorial(r))


if __name__ == "__main__":
    print(combination(52, 52))
