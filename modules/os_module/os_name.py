"""
os.name: The name of the operating system dependent module imported.
"""

import os


def get_pc_details() -> object:
    """
    Returns PC related information
    @return: object
    """
    return os.uname()


if __name__ == "__main__":
    pass
