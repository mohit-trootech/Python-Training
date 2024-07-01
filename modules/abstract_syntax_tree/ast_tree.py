import ast

tree = ast.parse("print('hello world')")

for node in ast.walk(tree):
    print(node)
    print(vars(node))
print(ast.walk(tree))
