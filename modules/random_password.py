"""
using secret choice to generate random password
"""

import secrets
import string
from time import sleep
from Python_Learning.password_validation_module import validate


def generate_password():
    character_set = string.ascii_letters + string.digits + string.punctuation
    while True:
        pas = "".join(secrets.choice(character_set) for i in range(64))
        if (
            any([c for c in pas if c in string.ascii_lowercase])
            and any([c for c in pas if c in string.ascii_uppercase])
            and any([c for c in pas if c in string.digits])
            and any([c for c in pas if c in string.punctuation])
        ):
            return pas


if __name__ == "__main__":
    generate_password()
    while True:
        password = generate_password()
        print(password, validate(password))
        sleep(1)
