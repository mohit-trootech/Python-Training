"""
re escape: It escapes the special character in the pattern.
"""

import re

print("File Path", __file__)
print(re.escape(__file__ + "\jijiji"))
