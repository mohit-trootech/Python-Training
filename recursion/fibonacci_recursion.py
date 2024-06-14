# Python Program to Generate Fibonacci Series using recursion

def fibonacci_series_recursion(size):
    if size <= 1:
        return size
    return fibonacci_series_recursion(size - 1) + fibonacci_series_recursion(size - 2)


for i in range(5):
    print(fibonacci_series_recursion(i), end=" ")
