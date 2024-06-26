"""
iter: create an iterator object with iterables in python
this approach is used to traverse a list with an efficient manner
"""
#
#
# class IteratorClass:
#
#     def __init__(self, iterable):
#         self.iterable = iterable
#
#     def __iter__(self):
#         self.iterable = iter(self.iterable)
#
#     def __next__(self):
#         return next(self.iterable)
#
#
# obj = IteratorClass([1, 2, 3, 4, 5, 6])
# print(obj)
# obj.__iter__()
# print(obj.__next__())
# print(next(obj.iterable))
# print(next(obj.iterable))
# print(next(obj.iterable))
# print(next(obj.iterable))
# print(next(obj.iterable))

# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# x = iter(my_list)
# print("Type:", type(x))
# #Method: 1
# for i in x:
#     print(i)

#Method: 2
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x)) #StepIteration


def read_file():
    try:
        with open('random.json', 'r') as f:
            x = iter(f.readlines())
            while True:
                userinput = input()
                if all(userinput):
                    print(next(x))
                else:
                    return
    except StopIteration:
        print("File Ended")

read_file()