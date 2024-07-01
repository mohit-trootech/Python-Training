st1 = {3, 4, 5, 21, 1, 41, 43, 53, 1, 432, 2, 24, 24, 24, 1, 12, 4, 5}
st2 = {i for i in range(5, 10)}
print(type(st1), st1)
print(type(st2), st2)
print(set(map(int.__mul__, st1, st2)))
print(set(map(int.__add__, st1, st2)))
print(set(map(int.__sub__, st1, st2)))
print(set(map(int.__sub__, st2, st1)))
print(set(map(int.__divmod__, st1, st2)))
print(set(map(int.__truediv__, st1, st2)))
print(set(map(int.__floordiv__, st1, st2)))
print(set(map(int.__floordiv__, st2, st1)))
