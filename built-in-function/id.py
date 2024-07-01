"""
id: returns the id of variables
"""

from copy import deepcopy
from getpass import getpass

pwd = getpass("Enter Password: ")
print(pwd)


def main():
    print("Hello")


f = main
# print(id(main))
# print(id(f))

a = 1
b = a
c = deepcopy(a)

# print(id(a), id(b), id(c))

lst1 = [1, 2, 3, 4, 5]
lst2 = lst1
lst3 = deepcopy(lst1)

# print(id(lst1), id(lst2), id(lst3))
# print(globals())
