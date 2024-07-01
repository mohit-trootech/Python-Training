"""A label associated with a variable, a class attribute or a function parameter or return value, used by convention
as a type hint."""

print(any.__class__)


class Car:
    wheels = 4

    def __init__(self) -> None:
        self.name = None

    def set_car_name(self, name: any) -> None:
        self.name = name


obj = Car()
obj.set_car_name("Audi")
print(obj.set_car_name.__annotations__)


def fib(n: int, output: list) -> list:
    if n == 0:
        return output
    else:
        if len(output) < 2:
            output.append(1)
            fib(n - 1, output)
        else:
            last = output[-1]
            second_last = output[-2]
            output.append(last + second_last)
            fib(n - 1, output)
        return output


print(__file__.__contains__)
print(fib.__annotations__)
