"""
delattr: function to delete the attribute of a class
"""


class Car:
    wheels = 4

    def __init__(self):
        self.speed = '45'


c1 = Car()
print(c1.wheels, c1.speed)
delattr(c1, 'speed')  # equivalent -> del c1.speed
# print(c1.wheels, c1.speed)
# delattr(c1, 'wheels')  # AttributeError
delattr(Car, 'wheels')  # AttributeError
# print(Car.wheels)  # AttributeError

