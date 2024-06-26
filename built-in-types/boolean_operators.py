"""
boolean: boolean expressions use True and False to work with if-else statements
Any object is considered as True 
Except if bool() return False or len() return 0
constants defined to be false: None and False.
zero of any numeric type: 0, 0.0, 0j, Decimal(0), Fraction(0, 1)
empty sequences and collections: '', (), [], {}, set(), range(0)
"""

# or: return first occurred True Value
print("" or False or True or "Mohit" or 1)  # return first True value
print("" or False or 0 or "Mohit" or 1)  # return first True value
print("" or False or 0 or "" or 1)  # return first True value
print("" or False or 0 or "" or None or "None")  # return first True value

# and: return first occurred False Value
print("Mohit" and 0 and 1 and True and False and () and [])
print("Mohit" and 1 and True and False and () and [])
print("Mohit" and 1 and True and True and () and [])
print("Mohit" and 1 and True and -2 and (6 + 5j) and [])
print("Mohit" and 1 and None and True and -2 and (6 + 5j) and [])
