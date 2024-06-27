"""
ArithmeticError: base class for error raise for various arithmetic operations
ArithmeticError inherits Exception
ArithmeticError inherited by OverflowError, ZeroDivisionError, FloatingPointError
"""

print(0.2 + 0.1 == 0.3)  # Floating Point Precision

try:
    print(5 / 4)
    print(5 / 0)
except ZeroDivisionError:
    print("Denominator Can't Zero")

print("3 power 64", 2**64)
print("3 power 128", 2**128)
print("3 power 256", 2**256)
print("3 power 512", 2**512)
print("Overflow Error Below")
print("3 power 1024", float(2**1024))
