"""
str: function to return str object when an object is called
"""


class ABC:

    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return "Hello"

    def __repr__(self):
        return f'ABC({self.msg!r}'


obj = ABC("Hi")
print(obj)
print(obj.__repr__())
