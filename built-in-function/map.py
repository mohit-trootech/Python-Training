"""
map: function used to map the element of iterable based on given logic
"""
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]

m = list(map(lambda x: x ** 2, lst))
print(lst, "->", m)
print("Equivalent to Write")
print([i**2 for i in lst])