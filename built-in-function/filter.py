"""
filter: function used to filter the iterable based on given condition
"""
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]

f = list(filter(lambda x: x % 2 == 0, lst))
print(lst, "->", f)
print("Equivalent to Write")
print([i for i in lst if i % 2 == 0])