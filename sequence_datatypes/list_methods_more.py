# """
# add, subtract, multiply, division of list
# """
#
# from functools import reduce
#
# b = {7, 8, 9, 10, 11, 12, 12}
# a = (1, 2, 3, 4, 5, 6, 7)
# d = {i: i**2 for i in range(1, 6)}
#
# result = map(int.__mul__, d, a)
# print(list(result))
# result = map(int.__mul__, d.values(), a)
# print(list(result))
# # result = map(int.__mul__, b, a)
# # print(list(result))
# # print(reduce(int.__add__, a))
# print(list(map(int.__add__, [1, 2, 3, 4], (1, 2, 3, 4))))
# print([*"hello"])
# # print([1, 2, 3, 4] + (1, 2, 3, 4))
class List:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        if len(self.value) == len(other):
            result = []
            try:
                for i in range(len(self.value)):
                    result.append(self.value[i] + other[i])
                return result
            except TypeError:
                print("Enter Same Type Elements in the List")
                return
        else:
            print("Both List Must be of Same Length")


obj = List([1, 2, 3, 4, 5])
print(obj + [1, 2, 3, 4, 5])  # Operator Overloading
print([1, 2, 3, 4, 5] + [1, 2, 3, 4, 5])
