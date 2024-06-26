"""
ascii - ASCII function returns the human-readable form of any string,
by converting non-ascii characters into ascii like - ç
"""
print(ascii(1))
print(ascii([1, 2, 3, 4]))
print(ascii("Hello"))
print(ascii('ç'))
print(ascii([1 + 2j]))
lst = [1, 2, 3, 'hi', 'ç']
print(list(map(ascii, lst)))
print(ascii(0b1000)) # Also Return Decimal Form of Any Binary Number
