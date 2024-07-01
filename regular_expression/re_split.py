"""
re split: used to split the string/Text from the given pattern and return list
"""

import re

text = "this is mohit working in trootech as a junior python developer"
pattern = ","
lst = re.split(pattern=pattern, string=text)
print(lst)
