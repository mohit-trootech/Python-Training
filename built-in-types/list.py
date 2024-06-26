"""
list: list are the python's sequence datatype that stored number of values with different datatypes in it.
@list function facilitates type conversion
@characteristics: mutable, ordered, allow duplicates
"""


class ListClass:
    """
    Implement List & List Methods
    """

    def __init__(self, lst: list) -> None:
        self.lst = lst

    @staticmethod
    def list_2_n(n: int) -> list:
        return [i for i in range(n)]

    def access_element_by_index(self, index: int) -> all:
        return self.lst[index]

    def remove_element_by_value(self, value: all) -> None:
        self.lst.remove(value)

    def remove_element_by_index(self, index: int) -> all:
        return self.lst.pop(index)

    def insert_element_at_end(self, value: all) -> None:
        self.lst.append(value)

    def insert_element_by_index(self, value: all, index: int) -> None:
        self.lst.insert(index, value)

    def copy_list(self) -> list:
        return self.lst.copy()

    def extend_list(self, values: list) -> None:
        self.lst.extend(values)

    def sort_list(self) -> None:
        self.lst.sort()

    def clear_list(self) -> None:
        self.lst.clear()

    def count_in_list(self, value: all) -> None:
        return self.lst.count(value)

    def slice_list(self, start=0, end=-1, step=1):
        return self.lst[start:end:step]


my_list_object = ListClass([1, 2, 3, 4, 5, 6, 'hi', 4 + 6j, (4, 4, 5), {5, 5, 2, '525'}])
my_list_object.extend_list([1, 99, 69])
copy_list = my_list_object.copy_list()
print(my_list_object.remove_element_by_index(6))
print(my_list_object.insert_element_by_index("Heloo", 6))
print(my_list_object.access_element_by_index(6))
print(my_list_object.slice_list(2))
print(copy_list)
print(my_list_object.lst)

# my_list = [1, 2, 3, 4, 5, 6, 7]
# print(type(my_list), list)
# List Comprehension
# print("List Comprehension: ", [i for i in range(10)])
