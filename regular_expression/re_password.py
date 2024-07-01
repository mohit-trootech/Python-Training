"""
re pattern to match passwords pattern
"""

from constants import words
import re

search = []
match = []
find = []
pattern = "((?=.*\d)(?=.*[A-Z])(?=.*[a-z])(?=.*\W)\w.{6,18}\w)"
for word in words:
    if re.search(pattern, word):
        search.append(re.search(pattern, word))
    if re.match(pattern, word):
        match.append(re.match(pattern, word))
    if re.findall(pattern, word):
        find.extend(re.findall(pattern, word))


print("Search", search)
print("Match", match)
print("Find", find, len(find))
print(len(words))
