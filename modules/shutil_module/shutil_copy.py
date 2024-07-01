"""
copy() function which is used to copy a data from one file to another.
no metadata is transfer just file content transfer
"""

import shutil
import constants
import os


# shutil.copy(constants.path + "copy.txt", constants.path + "copy1.txt")
shutil.copy2(constants.path + "copy.txt", constants.path + "copy2.txt")
import os

print(os.stat(constants.path + "copy.txt"))
print(os.stat(constants.path + "copy.txt"))
