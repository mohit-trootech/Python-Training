"""
hasattr: function to check the attribute available in that class
"""


class Car:
    wheels = 4

    def __init__(self):
        self.speed = '45'


c1 = Car()
print(hasattr(c1, 'speed'))
delattr(c1, 'speed')
print(hasattr(c1, 'speed'))
print(hasattr(Car, 'wheels'))
delattr(Car, 'wheels')
print(hasattr(Car, 'wheels'))
