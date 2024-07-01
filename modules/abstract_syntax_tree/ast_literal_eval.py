"""
literal eval: file the value of node stored as a string
"""

import ast

df = dict(enumerate([i for i in range(1, 10)], 11))
with open("testfile.txt", "w") as fp:
    fp.write(str(df))

with open("testfile.txt", "r") as fp:
    file_object = fp.read()
    print(file_object)
    print(type(file_object))

    print("With Literal Eval")
    literal_obj = ast.literal_eval(file_object)
    print(literal_obj)
    print(type(literal_obj))

    temp_int = ast.literal_eval("'5+6'")
    print(temp_int)
    # print(ast.literal_eval("5" + "6", type("5+6")))

# # ast.literal_eval("1+1")
# #
# obj = ast.literal_eval("True")
# print(obj)
# print(type(obj))
# print(ast.literal_eval("None"))
# print(type(ast.literal_eval("None")))
# # user_input = input("Enter: ")
# # result = ast.literal_eval(user_input)
# print(ast.literal_eval("6"))
# print(type(ast.literal_eval("5")))
# # print(result)
# # print(type(result))
