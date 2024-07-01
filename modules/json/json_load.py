"""
json.dump() method can be used for read to JSON file.
directly send file pointer as a argument to write content
"""

import json

data = {"name": "rahul", "age": 56, "cgpa": 8.6, "phone": "9999888222"}
print(data)
data.setdefault()
with open("jsondumpload.json", "r") as f:
    print(json.load(f))
