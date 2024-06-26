"""
to mitigate denial of service attack: Python limits the str length to convert into integer
"""
import sys

a = '5'  # lets create a variable 5
print(f"A: {a}")  # not as the str is numeric we can convert str to int
print("Similarly, a*50 Returns")
print(len(a * 50), int(a * 50))
print("whats the limit of this conversion: 4300! Means 4300 is Fine But not 4301")
try:
    print(len(a * 4301), int(a * 4301))
except ValueError as err:
    print(err)
print("Can we Change this Limit Yes from sys we can call set_int_max_str_digits() & Set Custom Limit")
sys.set_int_max_str_digits(5000)
print(len(a * 5000), int(a * 4301))
