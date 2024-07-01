"""Enumerations or Enums is a set of symbolic names bound to unique values. It can be iterated over to return its
canonical members in definition order. It provides a way to create more readable and self-documenting code by using
meaningful names instead of arbitrary values."""

from enum import Enum


class DateOption(Enum):
    USER_JSON = 1
    MOVIE_JSON = 2


# for i in DateOption:
#     print(i.value, i.name)
print(DateOption.USER_JSON.__class__)
a = 2
if a in [DateOption.USER_JSON.value, DateOption.MOVIE_JSON.value]:
    print(True)
else:

    print(False)


def sample(**kwargs):
    print(kwargs.__class__)


sample(password="password", name="name", age=a, email="email", role="role")
