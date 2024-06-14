# program to find types of class arguments
class ABC:
    name = "ABC"

    def __init__(self):
        self.name = "instance"


# class XYZ(ABC):
#
#     def test(self):
#         print(super().name+"XYZ")
class XYZ(ABC):
    name = "XYZ"


class ABCXYZ(XYZ):
    def get(self):
        print(super(ABC, self).__init__())


o1 = ABCXYZ()
o1.get()
# o1 = XYZ()
# o1.test()
#
# obj = ABC()
# print(obj.name)
# print(ABC.name)
# ABC.name = "Class variable"
# obj.name = "instance variable"
# print(ABC.name)
# print(obj.name)
