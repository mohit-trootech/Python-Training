# Simple Calculator Program
while True:
    operator = input("Choose the Follow Operations \n"
                     "1. Choose 1 for Addition\n"
                     "2. Choose 2 for Subtraction\n"
                     "3. Choose 3 for Multiplication\n"
                     "4. Choose 4 for Division\n"
                     "(Must be Integer Press C/c to Exit)- ")
    num1 = input("Enter The First Number (Must be Integer Press C/c to Exit) - ")
    num2 = input("Enter The Second Number (Must be Integer Press C/c to Exit) - ")
    if operator.isnumeric() and num1.isnumeric() and num2.isnumeric():
        num1 = int(num1)
        num2 = int(num2)
        break
    elif operator.lower() == 'c' or num1.lower() == 'c' or num2.lower() == 'c':
        print("You Entered C/c Program Closed")
        exit()
    else:
        print("Enter Valid Integer Input")

match operator:
    case '1':
        print(f"Addition = {num1+num2}")
    case '2':
        print(f"Subtraction = {num1-num2}")
    case '3':
        print(f"Multiplication = {num1*num2}")
    case '4':
        if num2 == 0:
            print("Zero Division Error Denominator Must be Greater Than 0")
        else:
            print(f"Division = {num1 / num2}")