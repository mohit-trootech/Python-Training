"""
re: pattern to find fixed length characters
"""

from constants import words
import re

search = []
match = []
find = []
pattern = "..... | ...."  # start with A and 5 more character
for word in words:
    if re.search(pattern, word):
        search.append(re.search(pattern, word))
    if re.match(pattern, word):
        match.append(re.match(pattern, word))
    if re.findall(pattern, word):
        find.extend(re.findall(pattern, word))


print("Search", search)
print("Match", match)
print("Find", find)
