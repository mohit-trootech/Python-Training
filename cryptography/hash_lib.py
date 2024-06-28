"""
This module implements a common interface to many different secure hash and message digest algorithms.
Included are the FIPS secure hash algorithms SHA1, SHA224, SHA256, SHA384, and SHA512 (defined in FIPS 180-2)
as well as RSA’s MD5 algorithm
RSA: Rivest, Shamir, Adleman, MD5: Message Digest 5 Algo
FIPS: Federal Information Processing Standard, SHA: Secure Hash Algorithm
"""

import hashlib
from hashlib import sha1, sha224, sha256, sha384, sha512

# print(hashlib.algorithms_guaranteed)
# print(hashlib.algorithms_available)
sha_1 = sha1()
sha_1_old = sha1()
sha_224 = sha224()
sha_256 = sha256()
sha_384 = sha384()
sha_512 = sha512()
print("SHA Objects")
# print(sha_1, sha_224, sha_256, sha_384, sha_512)
msg = b"MohitHello2001@"
sha_1.update(msg)
sha_1_old.update(msg)
print(sha_1 == sha_1_old)
sha_1.digest()
sha_1_old.digest()
print(sha_1 == sha_1_old)
# print(sha_1.block_size)
# print(sha_1.digest_size)
old = hash("Hello")
new = hash("Hello")
print(old == new)
