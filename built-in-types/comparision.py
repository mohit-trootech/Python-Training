"""
comparison: used to compare value
"""


class Compare:

    def __init__(self, value):
        self.value = value

    def __lt__(self, other):
        return self.value < other

    def __gt__(self, other):
        return self.value > other

    def __le__(self, other):
        return self.value <= other

    def __ge__(self, other):
        return self.value >= other

    def __eq__(self, other):
        if isinstance(other, self.value.__class__):
            return self.value == other
        else:
            return False

    def __ne__(self, other):
        if isinstance(other, self.value.__class__):
            return self.value != other
        else:
            return False

    def __isub__(self, other):
        return self.value is other


obj = Compare(5)
print(obj == 5)
print(obj <= 4)
print(obj < 10)
print(obj > 4)
print(obj >= -99)
print(obj != -99)
print(obj is Compare)
print(obj is obj)
