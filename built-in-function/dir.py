"""
dir: function is used to return all the methods & properties present in that scope
"""

counter = 0


print(globals().setdefault("name", "Mohit"))
print(globals())

def increment():
    print(globals().get("name"))
    x = 5
    print(dir())
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

