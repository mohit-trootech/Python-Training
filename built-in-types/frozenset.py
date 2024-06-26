"""
frozenset: immutable sets are known as frozen set
methods: all methods are available similar to set
Except: add, clear, remove etc. which alter the set
"""
fs = frozenset({1, 2, 3, 45, 5, 52, 62, 62, 626, 26, 62, 26, 26, 1, 136, 1, 136, 4})
print(fs.__class__, fs)
print("Len: ", fs.__len__())
print(3 in fs)
print(399 in fs)
