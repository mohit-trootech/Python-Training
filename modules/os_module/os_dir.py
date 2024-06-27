"""
os.mkdir() function is used to create new directory.
os.getcwd() function is used to return current working directory path.
"""

import os
from constants import path


def make_dir(dir_name):
    os.mkdir(dir_name)


def get_cwd():
    print(os.getcwd())


def change_dir(path):
    os.chdir(path)


if __name__ == "__main__":
    print(os.path.exists(path + "TestName1"))
    if not os.path.exists(path + "TestName1"):
        make_dir("TestName1")
    print(os.listdir(path))
    print(os.path.exists(path + "TestName1"))
    os.rmdir("TestName1")
    print(os.path.exists(path + "TestName1"))
    print(os.listdir(path))
    get_cwd()
    os.chdir("/home/trootech/Mohit/Python_Learning/modules/os_module/TestName")
    get_cwd()
