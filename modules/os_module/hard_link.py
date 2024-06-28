import os
from constants import path, file_path4, file_path3

# src = file_path4
#
# # Destination file path
# dst = file_path3
#
# os.link(src, dst)
#
# print("Hard link created successfully")
print(os.readlink(file_path4))
