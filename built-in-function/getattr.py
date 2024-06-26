"""
delattr: function to delete the attribute of a class
"""


class Car:
    wheels = 4

    def __init__(self):
        self.speed = '45'


c1 = Car()
print(c1.wheels, c1.speed)
print(getattr(c1, 'speed'))  # equivalent -> c1.speed
print(c1.wheels, c1.speed)
print(getattr(Car, 'wheels'))
print(Car.wheels)

