import json
import requests


# res = requests.get("https://letsenhance.io/static/8f5e523ee6b2479e26ecc91b9c25261e/1015f/MainAfter.jpg")
# res = requests.get("https://ik.imagekit.io/demo/sample-video.mp4")
res = requests.get("https://api.dictionaryapi.dev/api/v2/entries/en/one")
print(res.json())
res = requests.get("https://api.dictionaryapi.dev/api/v2/entries/en/hello")
print(res.json())
res = requests.get("https://api.dictionaryapi.dev/api/v2/entries/en/hello")
print(res.json())
res = requests.get("https://api.dictionaryapi.dev/api/v2/entries/en/hello")
print(res.json())

# f = open('v.mp4', "wb")
# f.write(res.content)



