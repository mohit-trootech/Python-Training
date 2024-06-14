import requests
import random
from multiprocessing import Process


def image_download():
    res = requests.get("https://picsum.photos/5000/5000.jpg")
    with open(f"testing{random.random()}.jpg", "wb") as f:
        f.write(res.content)


for i in range(50):
    p = Process(target=image_download)
    p.start()
