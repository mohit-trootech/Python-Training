# import os
# import sys
# import shutil
# import math
# import random
# import statistics
# from urllib.request import urlopen
# import html2text
# from bs4 import BeautifulSoup
# import datetime
# from string import Template
#
#
#
#
# #
# # with urlopen("https://en.wikipedia.org/wiki/India") as response:
# #     for line in response:
# #         line = line.decode()
# #         print(line)
# # soup = BeautifulSoup(urlopen("https://en.wikipedia.org/wiki/India").read())
# # print(soup)
# # # txt = soup.find('div', {'class' : 'body'})
# #
# # # print(html2text.html2text(txt))
#
# ---- pattern with nested loop ----
for row in range(1, 6):
    for col in range(1, row + 1):
        print("*", end="")
    print("")
for row in range(4, 0, -1):
    for col in range(1, row + 1):
        print("*", end="")
    print("")
