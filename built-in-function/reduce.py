"""
reduce: Reduce Method is used to reduce the sequence with given logic
"""
from functools import reduce
from operator import add, sub, mul, floordiv

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
lst.reverse()
print(lst)
print(reduce(add, lst))
print(reduce(sub, lst))
print(reduce(mul, lst))
print(reduce(floordiv, lst))
print(reduce(lambda a, b: a if a < b else b, lst))  # Minimum
print(reduce(lambda a, b: a if a > b else b, lst))  # Maximum

print(reduce(lambda a, b: True if bool(a and b) else False, [1, 2, 3, 4]))
print("Equivalent to", bool([1, 2, 3, 4]))

lst = [[1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]]

n_lst = reduce(list.__add__, lst, [])
print(reduce(lambda a, b: 10*a+b, n_lst))
