# Driver function
import os
import pprint
from time import sleep as s

if __name__ == "__main__":
    os.chdir("/home/trootech/Mohit/Python_Learning")
    for root, dirs, files in os.walk(".", topdown=True):
        pprint.pprint(root)
        pprint.pprint(dirs)
        pprint.pprint(files)
        s(2)
# # import os
#
# os.kill(81574)
