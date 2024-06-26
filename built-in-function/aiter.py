# """
# aiter - Asynchronous Iterator function: it is the built-in python function
# it is used to work with Asynchronous Iterable to return: Async object
# introduced in python version 3.10 to work with python
# """
#
# def num_to_n(n):
#     for i in range(1, n+1):
#         yield i
#
#
# iterable_obj = num_to_n(7)
import asyncio


#
#
# async def async_iter():
#     for i in range(1, 15):
#         await asyncio.sleep(2)
#         yield i
#
#
# x = async_iter()
# async def main():
#     async for i in aiter(x):
#         print(i)
#
# asyncio.run(main())
#
#
# class AsyncIteratorIO:
#
#     def __init__(self, data):
#         self.data = data
#         self.index = 0
#
#     def __aiter__(self):
#         return self
#
#     async def __anext__(self):
#         if self.index == len(self.data):
#             raise StopIteration
#         value = self.data[self.index]
#         self.index += 1
#         return value
#
#
# async def main():
#     async_obj = AsyncIteratorIO([1, 2, 3, 4, 5, 6, 7])
#     x = aiter(async_obj)
#     # print(await anext(x))
#     # print(await anext(x))
#     # print(await anext(x))
#     # print(await anext(x))
#     # print(await anext(x))
#     # print(await anext(x))
#     # print(await anext(x))
#     # equivalent to above
#     async for value in aiter(async_obj):
#         print(value)
#
#
# asyncio.run(main())


# Generate Random Numbers
from random import random


async def random_numbers(length):
    for i in range(length):
        yield random()


async def main():
    async for i in aiter(random_numbers(10)):
        print(i)


asyncio.run(main())
