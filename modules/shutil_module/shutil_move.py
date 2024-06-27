import os
import shutil
from time import sleep
from multiprocessing import Process


def file_move():
    while True:
        try:
            shutil.move("test", "testdir/")
        except shutil.Error:
            shutil.move("testdir/test", ".")


for i in range(10):
    sleep(1)
    p = Process(target=file_move)
    p.start()
