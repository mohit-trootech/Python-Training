# Filter Even & Odd Number Till User Input
from check_number_input import is_number
from even_odd_module import is_even


length = input("Enter the Last Number to Find - ")
if is_number(length):
    even_list = [i for i in range(int(length)) if is_even(int(i))]
    odd_list = [i for i in range(int(length)) if not is_even(int(i))]
    print(f"Result Lists Are Even List - {even_list}\nOdd List - {odd_list}")

