"""
dict: function used to generate a dictionary object
"""

my_dict = dict({1: "Hello", 2: "Namaste"})
print(my_dict)
key = [1, 2, 3]
value = ["one", "two", "three"]
Dict = dict(zip(key, value))
# print(dict(enumerate(value, 100)))
print(
    type(Dict.values()), Dict.values(), isinstance(Dict.values(), (dict, list, tuple))
)  # Values of Dictionary
print(type(Dict.keys()), Dict.keys())  # Key of Dictionary
print(Dict.fromkeys(key))  # Values of Dictionary
print(type(Dict.items()), Dict.items())  # Values of Dictionary
print(Dict.pop(1), Dict)  # Values of Dictionary
print(Dict.popitem(), "Dict->", Dict)  # Values of Dictionary
print(
    Dict.get(1)
)  # Return value of a key if available else Don't Throw Error return None
# print(Dict[1])  # Return value of a key if available else KeyError
