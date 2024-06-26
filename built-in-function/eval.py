"""
eval function is used to evaluate one line python code Debug & Return Output
return Same Error as the actual code
"""


def eval_code(code: str):
    return eval(code)


code_input = input("Enter the code: ")
print("Code Output", eval_code(code_input))

