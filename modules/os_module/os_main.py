"""os module: This module provides a portable way of using operating system dependent functionality. os.stat() method
os.stat() system calls on the specified path. This method is used to get the status of the specified
path."""

import os
from Python_Learning.modules.os_module import os_name
from constants import file_path4

path = "/home/trootech/Mohit/Python_Learning/modules/os_module/File4"
# print(os, os.__class__)
# print(dir(os))
# print(os.stat("/home/trootech/Mohit/Python_Learning"))
# print(os_name.get_pc_details())
# print(dir(os))
# print(os.stat(file_path4))
# import pathlib
#
# pathlib.Path.touch("file")
os.rmdir("newfile0")
