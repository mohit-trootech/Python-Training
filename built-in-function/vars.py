"""
vars: return the variable of object
"""
import os


class Person:
    pass


p = Person()
p.name = "Mohit"
p.age = 23
print(vars(p))
print(globals())
print(dir())
print(locals())
print(os.environ)
