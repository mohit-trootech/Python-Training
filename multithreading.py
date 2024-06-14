from threading import Thread
from time import sleep


def s1():
    for i in range(100):
        sleep(1)
        print("Hello")


def s2():
    for i in range(100):
        sleep(1)
        print("Hi")

#
# s1()
# s2()
t1 = Thread(target=s1)
t2 = Thread(target=s2)
t1.start()
t2.start()
t1.join()
t2.join()