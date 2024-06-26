"""
complex: function Used to Generate Complex Number with real & Imaginary Part
takes arguments as complex('1+1j'):str //OR// complex(1+1j)
Except: complex('1 + 1j'): ValueError
"""


def generate_complex_number(real: float, img: float) -> complex:
    return complex(real, img)


print(generate_complex_number(5, 4))
x = 9+7j
print(type(x), x)
# y = complex(6 + 8j)
y = 8
print(type(y), y)
z = -9.9+3j
print(type(z), z)
# print(complex('1 + 1j'))  # ValueError

a = 1+2j
b = 2+2j
print("Sum", a+b)
print("Sub", a-b)
print("Sub", b-a)
print("Mul", a*b)
print("Div", a/b)
print("Div", b/a)
