# Even Odd Number
while True:
    num = input("Enter The First Number (Must be Integer Press C/c to Exit)- ")
    if num.isdigit():
        num = int(num)
        if num%2 == 0:
            print(f"{num} is Even Number")
        else:
            print(f"{num} is Odd Number")
        break
    elif num.lower() == 'c':
        print("You Entered C/c Program Closed")
        exit()
    else:
        print("Enter Valid Integer Input")