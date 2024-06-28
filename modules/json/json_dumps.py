"""
json.dumps() method can be used for creating a json str.
To save that json string we need to use file handling write method
"""

import json

data = {"name": "rahul", "age": 56, "cgpa": 8.6, "phone": "9999888222", "status": True}
print(data.__class__)
print("Python Dict", data)
json_content = json.dumps(data)
print(json_content.__class__)
print("Json Str", json_content)
