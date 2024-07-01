"""
@classmethod: it is the decorator for a method in a class to make a method a class method

"""


class ABC:

    class_var = "Class Variable"

    def __init__(self):
        self.instance_var = "Instance Variable"

    def instance_method(self):
        print("Instance")
        print(self.instance_var)
        print(self.class_var)

    @classmethod
    def class_method(cls):
        print(cls.class_var)

    @staticmethod
    def static_method():
        print("Static")


obj = ABC()
obj.instance_method()
# ABC.instance_method()  #TypeError -> ABC().instance_method() works
obj.class_method()
ABC.class_method()
obj.static_method()
ABC.static_method()
ABC().static_method()
