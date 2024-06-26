"""
bin - Binary function: return the equivalent binary value of any integer number
params: exactly takes one argument
Except: str, complex, float
"""

print(bin(3))
print(bin(15))
# print(bin('hi')) #Error
print(list(map(bin, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])))
print(bin(-10))


def transfer_to_network(lst: list) -> None:
    print(list(map(bin, lst)))


transfer_to_network([1, 2, 3, 4, 5, 6, 7, 8, -10])
