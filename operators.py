"""
Operators are Symbols used to perform specific tasks.
Task Related to Arithmetic Operation, Assignment Operator, Conditional Operator etc.
+, -, /, //, *, **, % - these are various arithmetic operator
>, >=, <, <=, ==, != - these are various conditional operator
<<, >>, |, &, ^, ~ - these are various bit-wise operator
"""

print("Arithmetic Operator")
print("5+6", 5 + 6)
print("5-6", 5 - 6)
print("5*6", 5 * 6)
print("5**6", 5**6)
print("6/5", 5 / 6)
print("6//5", 5 // 6)
print("6%5", 6 % 5)

print("Conditional Operator")
print("5<6", 5 < 6)
print("5<=6", 5 <= 6)
print("5>6", 5 > 6)
print("5>=6", 5 >= 6)
print("5==6", 5 == 6)
print("5!=6", 5 != 6)

print("Bit-Wise Operator")
print("011&010", 1 & 0)
print("011|010", 1 | 0)
print("001^010", 1 ^ 0)
print("~0", ~14)
print("001>>1", 8 >> 1)
print("010>>1", 2 << 1)


# Python program to demonstrate
# operator overloading


class BitWiseExample:
    def __init__(self, value):
        self.value = value

    def __and__(self, obj):
        print("And operator overloaded")
        if isinstance(obj, BitWiseExample):
            return self.value & obj.value
        else:
            raise ValueError("Must be a object of class BitWiseExample")

    def __or__(self, obj):
        print("Or operator overloaded")
        if isinstance(obj, BitWiseExample):
            return self.value | obj.value
        else:
            raise ValueError("Must be a object of class BitWiseExample")

    def __xor__(self, obj):
        print("Xor operator overloaded")
        if isinstance(obj, BitWiseExample):
            return self.value ^ obj.value
        else:
            raise ValueError("Must be a object of class BitWiseExample")

    def __lshift__(self, obj):
        print("lshift operator overloaded")
        if isinstance(obj, BitWiseExample):
            return self.value << obj.value
        else:
            raise ValueError("Must be a object of class BitWiseExample")

    def __rshift__(self, obj):
        print("rshift operator overloaded")
        if isinstance(obj, BitWiseExample):
            return self.value >> obj.value
        else:
            raise ValueError("Must be a object of class BitWiseExample")

    def __invert__(self):
        print("Invert operator overloaded")
        return ~self.value


a = BitWiseExample(10)
b = BitWiseExample(12)
print(a & b)
print(a | b)
print(a ^ b)
print(a << b)
print(a >> b)
print(~a)
