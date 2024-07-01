a = {i: i**2 for i in range(1, 6)}
b = {i: i**3 for i in range(6, 9)}
print(a)
print(b)
# a = b.copy()
# print(a)
# a.update(b)
# print(dict(map(int.__add__, a, b)))
print(list(enumerate(b)))
x = {"a": 3}
y = {"a": 1}
print(dict(x, **y))
