lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(type(range(1, 2)))
a = slice(1, 50)
print(a)
print(lst[a])


def slice_list(start=0, stop=None, step=1):
    return lst[slice(start, stop, step)]


print(slice_list())
