"""
callable: function return: True if object is callable Else: False
"""


def my_func():
    print(5)


class ABC:
    # pass
    def __call__(self, *args, **kwargs):
        print("I am Called")


test = my_func


print(callable(my_func))
print(callable(test))
print(callable(5))
print(callable('my_func'))
print(callable([]))
print(callable(ABC))
abc_obj = ABC()
# print(abc_obj())
print(callable(abc_obj))
