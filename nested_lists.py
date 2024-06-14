# Nested List

nested = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for i in nested:
    print(i)

print("Matrix Transpose")
nested_comprehension = [[row[i] for row in nested] for i in range(3)]
for i in nested_comprehension:
    print(i)

    