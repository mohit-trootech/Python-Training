"""
os.remove() method in Python is used to remove or delete a file path.
"""

import os
import constants
from time import sleep

for i in range(5):
    with open(f"files{i}", "w+"):
        print(f"created files{i}")
        sleep(0.5)
    os.sync()
os.sync()
for i in range(5):
    os.remove(constants.path + f"files{i}")
    print(f"Removed newfile{i}")
    sleep(0.5)
    os.sync()
