"""
chr: function returns the character representation from ascii value i.e., ascii: 65 = A
"""


def ascii_2_chr(value: int) -> str:
    return chr(value)


# print(ascii_2_chr(65))
# print(ascii_2_chr(64))
# print(ascii_2_chr(-64))  #signed int: return Value Error
# print(list(map(chr, [33, 99999, 9999, 999])))
# print(chr(5+3j))  #complex: TypeError
# print(chr('65'))  #str: TypeError
print([ascii_2_chr(i) for i in range(33, 200)])
