# Python Program to Find Factorial using recursion


def factorial_recursion(num):
    if num == 1:
        return 1
    return num*factorial_recursion(num - 1)

print(factorial_recursion(5))


