"""
copy() function which is used to copy a data from one file to another.
no metadata is transfer just file content transfer
"""

import shutil
import constants


shutil.copy(constants.path + "copy.txt", constants.path + "copy.txt")
