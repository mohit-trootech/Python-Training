"""
global: function is used to work with global variables in python
"""

counter = 0


print(globals().setdefault("name", "Mohit"))
print(globals())


def increment():
    print(globals().get("name"))
    global counter
    counter += 1
print(dir())


def decrement():
    global counter
    counter -= 1


print(counter)
increment()
print(counter)
decrement()
print(counter)

