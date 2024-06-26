"""
issubclass: returns True if child class inherits the parent class
"""


class Animal:
    pass


class Bird(Animal):
    pass


class Cat:
    pass


print(issubclass(Cat, Animal))
print(issubclass(Bird, Animal))
