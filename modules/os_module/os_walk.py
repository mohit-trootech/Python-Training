# Driver function
import os
from time import sleep as s

if __name__ == "__main__":
    os.chdir("/home/trootech/Mohit/Python_Learning")
    for root, dirs, files in os.walk(".", topdown=True):
        print(root)
        print(dirs)
        print(files)
        print("--------------------------------")
        s(0.5)
# import os
#
# os.kill(81574)
