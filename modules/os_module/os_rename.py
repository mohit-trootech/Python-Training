"""
os.rename() function of OS module. This method renames a source file or directory to a specified destination file
or directory. It takes two parameters – source (current file name) and destination (new file name).
"""

import os
from constants import path, file_path3, file_path4

# os.link(path + "File1", path + "File3")
# os.rename(file_path3, path + "File1")

os.rename("/home/trootech/Mohit/Python_Learning/modules/home", path)
