# """
# property: used to create a property of class works with get, set, del property
# """
#
#
# class Bike:
#
#     def __init__(self):
#         self.__speed = None
#
#     @property
#     def get_speed(self):
#         """
#         I am Property
#         :return:
#         """
#         return self.__speed
#
#     @get_speed.setter
#     def get_speed(self, speed):
#         self.__speed = speed
#
#     @get_speed.deleter
#     def get_speed(self):
#         del self.__speed
#
#
# splendor = Bike()
# splendor.get_speed = 10
# print(splendor.get_speed)
# del splendor.get_speed
# # print(splendor.get_speed)  # Attribute Error
#
# class C:
#     def __init__(self):
#         self._value = None
#
#     @property
#     def x(self):
#         """I'm the 'x' property."""
#         return self._value
#
#     @x.setter
#     def x(self, value):
#         self._value = value
#
#     @x.deleter
#     def x(self):
#         del self._value
#
#
# c = C()
# print(c.x)
# c.x = "Hello"
# print(c.x)
# del c.x
# # print(c.x)  # AttributeError
#
#
# class Temerature:
#
#     def __init__(self):
#         self.__celcius = None
#
#     def get_temp(self):
#         return self.__celcius
#
#     def set_temp(self, temp):
#         self.__celcius = temp
#
#
# t = property(Temerature.get_temp)


class Distance(object):
    def __init__(self):
        # This private attribute will store the distance in metres
        # All units provided using setters will be converted before
        # being stored
        self._distance = 0.0

    @property
    def in_metres(self):
        return self._distance

    @in_metres.setter
    def in_metres(self, val):
        try:
            self._distance = float(val)
        except:
            raise ValueError("The input you have provided is not recognised "
                             "as a valid number")

    @property
    def in_feet(self):
        return self._distance * 3.2808399

    @in_feet.setter
    def in_feet(self, val):
        try:
            self._distance = float(val) / 3.2808399
        except:
            raise ValueError("The input you have provided is not recognised "
                             "as a valid number")

    @property
    def in_parsecs(self):
        return self._distance * 3.24078e-17

    @in_parsecs.setter
    def in_parsecs(self, val):
        try:
            self._distance = float(val) / 3.24078e-17
        except:
            raise ValueError("The input you have provided is not recognised "
                             "as a valid number")

d= Distance()

d.in_metres = 10
print(d.in_metres)
d.in_feet = 11
print(d.in_feet)