"""
bytearray: function returns the mutable bytearray object
bytearray[source, encoding, errors]
"""

print(bytearray(5))
print(bytearray([1, 2, 3]))
print(list(map(bytearray, [1, 2, 3])))
print(bytearray("Hello This is ByteArray", 'utf-8'))
print(bytearray("Hello This is ByteArray", 'utf-16'))
print(bytearray("Hello This is ByteArray", 'utf-32'))

x = bytearray(5)
print(f"x Before: {list(x)}")
x[0] = 99
print(f"x After: {list(x)}")


# Real life Application
msg = b""
data = b"Hello Hi Namaste"
msg += bytearray(data)
print(msg)


