"""
hashlib on file to hash it!
"""

import sys
import hashlib

sha256 = hashlib.sha256()


def hashfile(file: str):
    """
    function to hashfile
    """
    with open(file, "rb") as f:
        content = f.read()

        if not content:
            print("Empty File")
            return

        print(content.__len__())
        print(content.__sizeof__())
        print("File Content", content)
        sha256.update(content)
    return sha256.digest()


if __name__ == "__main__":
    file_hash = hashfile("plain.txt")
    print("file hash: ", file_hash)
    print(file_hash.__len__())
    print(file_hash.__sizeof__())
