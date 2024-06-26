"""
bool - Boolean function similar working as all & any return True for each
Except: empty iterable, 0, False, None
"""

print(bool(1))
print(bool(1.1))
print(bool(-1.1))
print(bool(-1 + 1j))
print(bool('hi'))
print(bool('ç'))
print(bool([1, 2, 3]))
print(bool([]))
print(bool(()))
print(bool(set()))
print(bool({}))
print(bool(0))
print(bool([0]))  #Return True
print(bool(None))
print(bool(False))


def is_list_empty(lst: list) -> bool:
    return not bool(lst)


print("Is List Empty?")
print([1, 2, 3], is_list_empty([1, 2, 3]))
print([], is_list_empty([]))

# Example
# user_input = bool(input("Are you hungry? True or false: "))
# print(type(user_input), user_input)
# if user_input:
#     print(" You need to eat some foods ")
# else:
#     print("Let's go for walk")


class Tree:
    def __init__(self, children):
        self.children = children

    def have_children(self):
        return bool(self.children)


obj = Tree(2)
print(obj.have_children())

obj = Tree(0)
print(obj.have_children())
