import os


os.open("mohit.txt", os.O_CREAT)
f = os.open("mohit.txt", os.O_RDONLY)

print(dir(f))
