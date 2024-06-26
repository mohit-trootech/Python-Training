# """
# compile: function make possible to compile the code dynamically
# compile(source:<str:file>, file:<str:file>, mode, flags, dont_inherit=False)
# """
# code1 = """print("hello! World")"""
#
#
# sum_to_n = """
# def sum_2_n(n):
#     return sum([i for i in range(n)])
# """
# exec(code1)
# exec(compile(code1, "<string>", "exec"))
# code = compile(sum_to_n, "<string>", "exec")
# exec(code)
# print(sum_2_n(50))

with open("compile_temp.py", "r") as f:
    code_str = f.read()
    code = compile(code_str, "compile_temp.py", 'exec')
    print(type(code))
    exec(code)

eval(compile('print("hello Python")', '', 'eval'))

