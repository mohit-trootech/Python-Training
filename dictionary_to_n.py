# Python Program to Create Dictionary i:i**i till n
from check_number_input import is_number

size = input("Enter the Size of Dictionary- ")
if is_number(size):
    size = int(size)
    my_dict = dict(zip([i for i in range(1, size)], [i**2 for i in range(1, size)]))
    print(my_dict)
