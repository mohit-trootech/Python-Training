"""
int: Integer Datatype Python
int class is {Whole Number}
"""


class IntClass:

    def __init__(self, value: int) -> None:
        if isinstance(value, int):
            self.value = value
        else:
            raise ValueError("Enter int Value")

    def __add__(self, other: int) -> int:
        if isinstance(other, int):
            return self.value + other
        else:
            TypeError("Enter int Value")

    def __sub__(self, other: int) -> int:
        if isinstance(other, int):
            return self.value - other
        else:
            TypeError("Enter int Value")

    def __mul__(self, other: int) -> int:
        if isinstance(other, int):
            return self.value - other
        else:
            TypeError("Enter int Value")

    def __truediv__(self, other):
        if bool(other):
            if isinstance(other, int):
                return self.value // other
            else:
                TypeError("Enter int Value")
        else:
            raise ZeroDivisionError("Denominator Must Not 0")

    def __floordiv__(self, other):
        if bool(other):
            if isinstance(other, int):
                return self.value // other
            else:
                TypeError("Enter int Value")
        else:
            raise ZeroDivisionError("Denominator Must Not 0")

    def __mod__(self, other):
        if bool(other):
            if isinstance(other, int):
                return self.value % other
            else:
                TypeError("Enter int Value")
        else:
            raise ZeroDivisionError("Integer Modulus Must Not 0")

    def __neg__(self):
        return -self.value

    def __str__(self):
        return f'{self.value}'


obj = IntClass(5)
print(obj)
print(obj + 5)
print(obj / 2)  # Truediv return floor div
print(obj // 2)
