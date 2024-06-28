"""
os.access: check user is authorized?
"""

from constants import file_path
import os


def check_access(path):
    if os.access(path, os.R_OK):
        with open(path, "r") as f:
            print(f.read())
    else:
        print("Not Authorized")


if __name__ == "__main__":
    check_access(file_path)
