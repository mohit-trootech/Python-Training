import ast

a = 5
x = "a + 3"
y = "3 + a"
print(x == y)
obj1 = ast.parse(x)
obj2 = ast.parse(y)
print(obj1)
print(obj2)

print([node for node in ast.walk(obj1)])
print([node for node in ast.walk(obj2)])
