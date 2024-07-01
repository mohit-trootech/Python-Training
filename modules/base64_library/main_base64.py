"""the base64 library offers functions for encoding and decoding binary data to and from base64 strings, effectively
converting any binary data to plain text."""

import base64


# def encodestring_main(msg):
#     return encodestring(msg)


def encode_simple(msg):
    return base64.b16encode(msg.encode())


def decode_simple(encrypt_msg):
    return base64.b16decode(encrypt_msg.decode())


message = "Hello Python !, From Java"
print("Message: ", message)
# print(encodestring_main(message))
e = encode_simple(message)
d = decode_simple(e)
print("Encoded: ", e)
print("Decoded: ", d)
