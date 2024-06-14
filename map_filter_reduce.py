# Map Filter Reduce Demonstration Program
from functools import reduce

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]

m = list(map(lambda x: x ** 2, lst))
print(m)

f = list(filter(lambda x: x % 2 == 0, lst))
print(f)

r = reduce(lambda x, y: x + y, lst)
print(r)
