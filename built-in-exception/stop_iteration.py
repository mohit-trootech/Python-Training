"""StopIteration: Error raise by generators and iterator object,
 to signal that there are no further items produced by the iterator.
 next() method is responsible to raise StopIteration
 """

lst = [1, 2, 3, 4]
iterator = iter(lst)

print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
try:
    print(next(iterator))
except StopIteration:
    print("StopIteration: there are no further items produced by the iterator.")


def generator_func(lst):
    for i in lst:
        yield i


generator_obj = generator_func(lst)
print(next(generator_obj))
print(next(generator_obj))
print(next(generator_obj))
print(next(generator_obj))
try:
    print(next(generator_obj))
except StopIteration:
    print("StopIteration: there are no further items produced by the iterator.")
