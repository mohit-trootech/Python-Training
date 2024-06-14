# Swap Number Without the use of New Variable
while True:
    num1 = input("Enter The First Number (Must be Integer Press C/c to Exit)- ")
    num2 = input("Enter The Second Number (Must be Integer Press C/c to Exit) - ")
    if num1.isnumeric() and num2.isnumeric():
        num1 = int(num1)
        num2 = int(num2)
        break
    elif num1.lower() == 'c' or num2.lower() == 'c':
        print("You Entered C/c Program Closed")
        exit()
    else:
        print("Enter Valid Integer Input")
print(f"Before Swapping Number 1 = {num1} & Number 2 = {num2}")
num1 = num1+num2
num2 = num1-num2
num1 = num1-num2
print(f"After Swapping Number 1 = {num1} & Number 2 = {num2}")
