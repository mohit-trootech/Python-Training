"""__doc__: A string literal which appears as the first expression in a class, function or module. While ignored when
the suite is executed, it is recognized by the compiler and put into the __doc__ attribute of the enclosing class,
function or module."""


class ABC:
    """Docstring First"""

    def __init__(self):
        pass


print(ABC.__doc__)
obj = ABC()
print(obj.__doc__)
