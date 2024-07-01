"""
hash: function to return has value of objects
"""

from copy import deepcopy


class MyClass:

    def __init__(self, value):
        self.value = value

    # def __hash__(self):
    #     return id(self.value)


obj = MyClass(5)
print(obj.value)
h = obj.__hash__()
print(h)

a = "hi"
b = a
c = "hi"
print(hash(hash(a)))
print(hash(hash(b)))
print(hash(a))
print(hash(b))
print(hash(c))
print(hash("Hi"))


list1 = [1, 2, 3, 4, 5]
list2 = deepcopy(list1)
list2.append(2)
print(list1, list2)
if hash(tuple(list1)) == hash(tuple(list2)):
    print("True")
else:
    print(False)
