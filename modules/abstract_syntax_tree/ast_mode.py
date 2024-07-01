"""
exec - This mode is used to execute the normal Python code.
eval - This mode is used to evaluate Python's expression and will return the result after evaluation.
single - This mode works as Python shell that executes one statement at a time.
"""

import ast


def ast_exec(c):
    c = ast.parse(c, mode="exec")
    return compile(c, filename="", mode="exec")


def ast_eval(c):
    c = ast.parse(c, mode="eval")
    return compile(c, filename="", mode="eval")


code = "for i in range(6): print(i)"
exec(ast_exec(code))
print(ast.dump(ast.parse("5 + 6")))
print(eval(ast_eval("5 + 6")))
print(eval("5 + 6"))
