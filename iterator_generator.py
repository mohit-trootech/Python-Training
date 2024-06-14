# Iterators & Generators Examples
def getnumber():
    for i in range(5):
        yield i

x = getnumber()
print(next(x))
print(next(x))
print(next(x))
