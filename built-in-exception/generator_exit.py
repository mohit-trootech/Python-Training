"""
GeneratorExit: Raised when Generator execution is closed/exited before its normal execution.
GeneratorExit inherits BaseException
"""

print(issubclass(GeneratorExit, BaseException))
print(issubclass(GeneratorExit, Exception))


def my_generator():
    try:
        yield 1
        yield 2
        yield 3
    except GeneratorExit:
        print("Generator Exit")


generator_obj = my_generator()
print(generator_obj.__class__)
print(generator_obj)
print(next(generator_obj))
generator_obj.close()
