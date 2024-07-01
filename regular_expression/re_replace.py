"""
re replace: replace is used to find the pattern and replace with matching character
"""

import re

pattern = "java"

text = "java is best programming language, java is number 1, Java"
print(
    re.sub(
        pattern=pattern,
        repl="Python",
        string=text,
    )
)
print(
    re.subn(
        pattern=pattern,
        repl="Python",
        string=text,
    )
)
