"""
isinstance: returns if the parameter datatype present in given instance
"""


class Animal:
    pass


class Bird(Animal):
    pass


class Cat:
    pass


def check_instance(value: all, instance: tuple) -> bool:
    return isinstance(value, instance)


obj = Bird()
cat_obj = Cat()
print(check_instance(4, (str, int)))
print(check_instance({}, set))
print(check_instance(set(), set))
print(check_instance(obj, Animal))
print(check_instance(cat_obj, Animal))
