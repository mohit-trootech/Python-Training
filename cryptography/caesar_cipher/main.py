"""
Caesar Cipher: one of the Most Common Cryptography algorithm Used for Encryption and Decryption Process
"""

import constant
from dotenv import dotenv_values
from encryption import encryption
from decryption import decryption

print("Available Keys")
print(constant.KEYS_2)
print(constant.KEYS_3)
config = dotenv_values(".env")
plain_text = input(r"Enter Secret Message: ")
cipher = encryption(plain_text, constant.KEYS_3[5])
print("Cipher Text: ", cipher)
plain_text = decryption(cipher, constant.KEYS_3[5])
print("Decrypted Plain Text: ", plain_text)
