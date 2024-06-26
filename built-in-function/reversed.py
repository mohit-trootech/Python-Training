"""
reversed: return reverse object of any sequence
"""


def reverse_object(data: all):
    return reversed(data)


x = reverse_object([1, 2, 3, 42, 315, 315, 161])
print(type(x))
print(list(x))
y = reverse_object("Helli")
print(y)
print(list(y))
