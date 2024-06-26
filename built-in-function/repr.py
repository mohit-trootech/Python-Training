"""
repr: works with class and return printable representation of string
"""


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"Person(name='{self.name}', age={self.age})"


person = Person("John", 25)
print(person)
print(repr(person))