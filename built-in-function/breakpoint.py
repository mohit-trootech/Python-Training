"""
breakpoint - Python Breakpoint function is used to create breakpoint during a debugging process
similar to import pdb; pdb.set_trace()
h: help
c: continue execution
q: quit Debugging
n: next line within the same function
s: next line within the same function or call another function
w:  current pointer line
l: list of current location
"""
from pdb import set_trace

n = 10

for i in range(n):
    breakpoint()
    print(i)
##
##

def hello():
    print("Hello")
