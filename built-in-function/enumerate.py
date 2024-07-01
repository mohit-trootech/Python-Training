"""
enumerate: function that return enumerate object that supports iteration
@params: iterable
enumerate object iterable object that have counter
"""

iterable = ["hi", [1, 2, 3, 4], (1, 2, 3, 4), "Namaste", "\\n", 2, 3, 4, "t\\t", 5 + 2j]
enum_obj = enumerate(iterable, 11)
print(type(enum_obj), enum_obj)
for i, j in enum_obj:
    print(i, j)

with open("demo.txt", "r") as f:
    content = f.readlines()
    enum_content = enumerate(content, 1)
    for line, line_content in enum_content:
        print(line, line_content)
