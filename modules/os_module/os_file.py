import os


os.open("new", os.O_CREAT)
f = os.open("new.txt", os.O_RDONLY)
print(f)
# print(dir(f))
