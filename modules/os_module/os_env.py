import os
from constants import file_path3
import sys

print(os.environ)
# os.execl(sys.executable, "python", __file__, *sys.argv[1:])
print(os.getcwdb())
print(os.fchown(file_path3))
# x = os.fdopen(1, file_path3)
# print(x.read())
