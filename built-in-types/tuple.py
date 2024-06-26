"""
tuple: tuple are the python's sequence datatype that stored number of values with different datatypes in it.
@tuple function facilitates type conversion
@characteristics: immutable, ordered, allow duplicates
"""

new_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, "Mohit", 2 + 4j)
print("we Use Round Brackets to Generate tuple")
print(new_tuple.__class__, new_tuple)
print("we can use in in Tuple")
print(5 in new_tuple)
print(10 in new_tuple)
print("Hash Value of Tuple", hash(new_tuple))
