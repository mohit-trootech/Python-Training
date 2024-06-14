# # # def f1(self):
# # #     print("Hello")
# # #
# # #
# # # class Test:
# # #     var1 = "NEWS"
# # #     var2 = "MODI"
# # #
# # #     f = f1
# # #
# # #
# # # o1 = Test()
# # # print(o1.var1, o1.var2)
# # # o2 = Test()
# # # print(o2.var1, o2.var2)
# # # o2.var2 = "PM MODI"
# # # print(o1.var1, o1.var2)
# # # print(o2.var1, o2.var2)
# # #
# # # class ABC:
# # #
# # #     def __init__(self):
# # #         self.__var = "Hello"
# # #
# # #
# # # obj = ABC()
# # # obj._ABC__var = "Nina"
# # # print(obj._ABC__var)
# #
# # from dataclasses import dataclass
# #
# # @dataclass
# # class Employee:
# #     name: str
# #     age: str
# #
# # e1 = Employee("Mohit",23)
# # print(e1.name)
#
#
# things = [1, 2, 3, 4, 5]
# boxes = iter([Box(size=2), Box(size=1), Box(size=3)])
# box = next(boxes)
#
# for thing in things:
#     box.put(thing)
#     if box.is_full:
#         box = next(boxes)


class XYZ:
    def __init__(self, a):
        self.a = "Test"
class ABC(XYZ):

    def __init__(self, a):
        super()
        self.a = "Hello"


obj1 = XYZ("a")
obj2 = ABC("a")
print(obj1.a)
print(obj2.a)
