"""
json.dumps() method can be used for creating a json str.
To save that json string we need to use file handling read method
"""

import json

json_content = (
    '{"name": "rahul", "age": 56, "cgpa": 8.6, "phone": "9999888222", "status":true}'
)
print(json_content.__class__)
print("Json Str", json_content)
data = json.loads(json_content)
print(data.__class__)
print("Python Dict", data)
