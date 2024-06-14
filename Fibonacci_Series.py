# Python Program for Fibonacci Series - Please Enter Number Input
lst = [0, 1]
while True:
    size = input("Enter the Size of Series ( Must be Integer Press C/c to Close - ")
    if size.isnumeric():
        size = int(size)
        break
    elif size.lower() == 'c':
        print("You Entered C/c Program Closed")
        exit()
    else:
        print("Enter a Integer Number Input")


for i in range(size-2):
    lst.append(lst[-1]+lst[-2])

print(f"Fibonacci Series - {lst}")