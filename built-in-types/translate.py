"""
create a translate object to return translate
"""
print("Translate")
translate = str.maketrans({"K": "F", "F": "K"})
print("Kung Fu Panda".translate(translate))
