# Python Program to Find Prime Number
while True:
    num = input("Enter The First Number (Must be Integer Press C/c to Exit)- ")
    if num.isnumeric():
        num = int(num)
        break
    elif num.lower() == 'c':
        print("You Entered C/c Program Closed")
        exit()
    else:
        print("Enter Valid Integer Input")

print("You Entered {}".format(num))

for i in range(2, num):
    if num == 1:
        print(f"{num} is Not Prime nor Composite")
    elif num == 2 or num == 3:
        print(f"{num} is Prime")
        break
    elif num % i == 0:
        print(f"{num} is Composite")
        break
else:
    print(f"{num} is Prime Number")

