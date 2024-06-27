"""os.removedirs() method in Python is used to remove directories recursively. If the leaf directory in the specified
path is successfully removed, then os.removedirs() tries to successively remove every parent directory mentioned in
path until an error is raised. The raised error is ignored because generally error is raised because directory to be
deleted is not empty."""

import os
import constants
from time import sleep

for i in range(5):
    os.mkdir(f"newfile{i}")
    print(f"created newfile{i}")
    sleep(0.5)
for i in range(5):
    os.removedirs(constants.path + f"newfile{i}")
    print(f"Removed newfile{i}")
    sleep(0.5)
