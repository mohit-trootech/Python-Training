"""
import__: function is used to import module
"""
import importlib

x = importlib.import_module('random')
print(x.randint(1,10))
x = __import__('random', globals(), locals(), [], 0)
print(x.random())
# print(x, globals(), locals(), [])
def main():
    return "10"

print(locals())
print(globals()['main'])
print(globals()['main']())
print(main())
