"""
bytes: function returns the immutable bytes object
bytes[source, encoding, errors]
"""

print(bytes(5))
print(bytes([1, 2, 3]))
print(list(map(bytes, [1, 2, 3])))
print(bytes("Hello This is bytes", "utf-8"))
print(bytes("Hello This is bytes", "utf-16"))
print(bytes("Hello This is bytes", "utf-32"))

x = bytes(5)
print(f"x Before: {list(x)}")
# x[0] = 99
# Cannot be Change Once Created
# print(f"x After: {list(x)}")


# Real life Application
msg = b""
data = b"Hello Hi Namaste"
msg += bytes(data)
msg.replace(b"Hi", b"Mohit")
print(msg)
