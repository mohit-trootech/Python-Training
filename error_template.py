# import sys
#
# try:
#     f = open('file')
#     s = f.readline()
#     i = int(s.strip())
# except OSError as err:
#     print("OS error: {0}".format(err))
# except ValueError:
#     print("Could not convert data to an integer.")
# except BaseException as err:
#     print(f"Unexpected {err=}, {type(err)=}")
#     raise

class InvalidAgeException(Exception):
    pass


try:
    raise InvalidAgeException("This is Error Message")
except InvalidAgeException as err:
    print('Handling run-time error:', err)

