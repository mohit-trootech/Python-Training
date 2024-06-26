"""
fabs - Floating Absolute function: similar to abs function always return: float, irrespective of parameter
usage: import from math module
real life implementation: use when you wanted to work with floating points rather then int
"""
from math import fabs

a = 1
b = -1
c = 2
d = 1 + 2j
# e = 'hi'
# f = [1, -1, 2.2, -2.2, 2 + 2j, -2 + 2j, 2 - 2j]
f = [1, -1, 2.2, -2.2]

print(type(a), fabs(a))
print(type(b), fabs(b))
print(type(c), fabs(c))
# print(type(d), fabs(d)) #not work with complex number
# print(type(e), fabs(e)) #return error since e:str
print(type(f), list(map(fabs, f)))  #use a map for list
