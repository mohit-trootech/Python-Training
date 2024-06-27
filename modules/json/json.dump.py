"""
json.dump() method can be used for writing to JSON file.
directly send file pointer as a argument to write content
"""

import json

data = {"name": "rahul", "age": 56, "cgpa": 8.6, "phone": "9999888222"}
print(data)
with open("jsondumpload.json", "r+") as f:
    json.dump(data, f, indent=3)
