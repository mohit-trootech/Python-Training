"""
pathlib: module offers classes representing filesystem paths with semantics appropriate for different operating systems.
"""

import pathlib
import os

# print(pathlib.__class__)
# print(vars(pathlib))
print(pathlib.Path.cwd())
print(pathlib.Path.home())
print(pathlib.Path(__file__).parent)
print(os.getcwd() + "/home")
print("Os Path Join")
print(os.path.join(os.getcwd() + "/home"))
print("pathlib join path")
print(pathlib.Path.cwd().joinpath("Mohit", "Python_learning"))
test = pathlib.Path.cwd().joinpath("Mohit", "Python_learning")
print(test.exists())
test = pathlib.Path.cwd()
print(test.is_dir())
print(pathlib.Path(__file__).exists())
test = pathlib.Path.cwd().joinpath("Mohit", "Python_learning", "test.txt")
print(test.is_dir())
print(pathlib.Path.cwd().with_suffix(".txt"))
txt = pathlib.Path("/Python_Learning/modules/pathlib_module/hello.txt")
print(txt)
<<<<<<< HEAD
py = txt.with_suffix(".txt")
=======
py = txt.with_suffix(".py")
>>>>>>> 0ffce43 ([Pathlib])
print(py)
# pathlib.Path.replace(txt, py)
