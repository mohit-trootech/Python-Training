"""
exec function is used to evaluate multiple line python code Debug & Return Output
return Same Error as the actual code
"""


def exec_code(code: str):
    return exec(code)


c = "import os \nos.getcwd()"
# code_input = input("Enter the code: ")
print("Code Output", exec_code(c))

