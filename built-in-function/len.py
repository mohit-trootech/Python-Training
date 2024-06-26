"""
len: return the length of object
@params: must be sequence or collection
"""

print(len([1, 2, 3]))
print(len(["1, 2, 3"]))
print(len("1, 2, 3"))
print(len(("1, 2, 3", "2, 3, 4")))
print(len(("1, 2, 3")))
print(len({"1, 2, 3"}))
print(len({"1, 2, 3": 1}))
# print(len(2)) #typeError
