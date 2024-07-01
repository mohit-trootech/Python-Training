"""Abstract Syntax Tree, which is a potent tool of the Python programming language. It allows us to interact with the
Python code itself and can modify it."""

import ast
from pprint import pprint

print(ast)
# print(ast.__doc__)
# pprint(dir(ast))
# print(vars(ast))

string_l = "[3, 2, 3, 4]"
print(ast.dump(ast.parse(string_l, filename="", mode="eval")))
print(ast.literal_eval(string_l))
list_object = ast.literal_eval(string_l)
print(list_object)
print(type(list_object))

ast_traverse = ast.walk(ast.parse(string_l, filename="", mode="eval"))
print(ast_traverse)
for node in ast_traverse:
    print(node)


datamap = ast.literal_eval("[1, 2, 3]")
if not isinstance(datamap, dict):
    print(datamap)
