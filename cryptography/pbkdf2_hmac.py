"""
hashlib on file to hash it!
"""

import sys
from hashlib import pbkdf2_hmac
import binascii

pbk1 = pbkdf2_hmac("sha256", b"Hello", b"f*Bj%(>nP5", 100000)

dk = binascii.hexlify(pbk1)

pbk3 = pbkdf2_hmac("sha256", b"Hello", b"f*Bj%(>nP5", 100000)

pbk3 = binascii.hexlify(pbk3)
print(pbk3 == dk)
# pbk2 = pbkdf2_hmac("sha256", b"password", b"HiI", 100000)
#
# dk = binascii.hexlify(pbk2)
# print(dk)
