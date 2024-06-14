from functools import reduce
import math


def lcm(*args):
    """python Program to find lcm"""
    return reduce(lambda a,b: a*b, args)//math.gcd(*args)


if __name__ == "__main__":
    print(lcm(79, 10))
