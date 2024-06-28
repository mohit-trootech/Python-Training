"""Pdb is a powerful tool for finding syntax errors, spelling mistakes, missing code, and other issues in your Python
code. pdb module is used to do the debugging in the Python which comes built-in to the Python standard library. The
pdb is defined as class Pdb which internally makes use of bdb (basic debugger functions) and cmd (support for
line-oriented command interpreters) modules."""

import pdb


def add(a, b):
    ans = a + b
    return ans


pdb.set_trace()
x = input("Enter first number : ")
y = input("Enter second number : ")
sum = add(x, y)
print(sum)
