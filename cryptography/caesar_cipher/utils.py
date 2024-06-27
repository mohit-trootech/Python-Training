"""
Utility file to store Custom Exception and Function
"""


class EmptyString(BaseException):
    def __init__(self, msg):
        super(EmptyString, self).__init__(msg)
