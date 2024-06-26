"""
dictionary: datatype in python to store the values in key-value pairs
dictionary can be created using the following methods
- key-value pairs
- dictionary comprehension
- type constructor
"""


class MyDict:

    def __init__(self):
        self.dictionary = None

    def key_value_pair(self, **kwargs) -> None:
        """
        Method to create dictionary with key-value pairs
        @param kwargs: {Key:Value}
        @return: None
        """
        self.dictionary = dict(**kwargs)

    def dict_comprehension(self, logic: str) -> None:
        """
        Method to create dictionary with dictionary comprehension
        @param logic: str
        @return: None
        """
        self.dictionary = eval("{{{logic}}}".format(logic=logic))

    def type_constructor(self, lst1: list, lst2: list) -> None:
        """
        Method to create Dictionary with type constructor
        @param lst1: list
        @param lst2: list
        @return: None
        """
        self.dictionary = dict(zip(lst1, lst2))


key_value_dict = MyDict()
key_value_dict.key_value_pair(Name="Mohit", Age=32, City="Ahmedabad")
print(key_value_dict.dictionary)
print(len(key_value_dict.dictionary))  # length of dictionary
print(list(key_value_dict.dictionary))  # list(dict) returns all the key used in the dictionary
print(key_value_dict.dictionary.values())  # dict.values() return all the values in the dictionary
print(key_value_dict.dictionary.keys())  # dict.keys() return all the key in the dictionary
print(key_value_dict.dictionary["Name"])  # dict['key'] return value for the given key else KeyError
print(key_value_dict.dictionary.get("Name"))  # dict.get('key') return value for the given key else None
print(key_value_dict.dictionary.get("Name"))  # dict.get('key') return value for the given key else None
del key_value_dict.dictionary['Name']  # Delete the Key and Value Pair
try:
    print(key_value_dict.dictionary["Name"])
except KeyError as e:
    print("Key Not Found", e)
print(key_value_dict.dictionary)
print("Name" in key_value_dict.dictionary)
print("Age" in key_value_dict.dictionary)
# dict_comprehension = MyDict()
# dict_comprehension.dict_comprehension("i:i**3 for i in range(1, 20)")
# type_constructor = MyDict()
# type_constructor.type_constructor([1, 2, 3, 4], ["one", "two", "three", "four"])
# print(dict_comprehension.dictionary)
# print(type_constructor.dictionary)
