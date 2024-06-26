"""
div mod: takes two non-complex numbers and return (quotient & remainder) both at once
"""


def div_and_mod(a: float, b: float) -> tuple:
    return a // b, a % b


x = 8
y = 3
print(div_and_mod(x, y))
print(divmod(x, y))
print(div_and_mod(12, 11))
print(divmod(12, 11))
print(div_and_mod(99, 17))
print(divmod(99, 17))
print("Floating Points")
print(div_and_mod(99.9, 17.9))
print(divmod(99.9, 17.9))
print("complex numbers")  # TypeError
# print(div_and_mod(1+1j, 2+2j))
# print(divmod(1+1j, 2+2j))
