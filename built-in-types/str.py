"""
str: function to return str object when an object is called
"""


class StrClass:

    def __init__(self, txt: str):
        self.txt = txt

    def index_word(self, word: str) -> int:
        """
        methods return first occurrence of index of words occurred in txt
        @param word: str
        @return: int
        """
        try:
            return self.txt.index(word)
        except ValueError as ve:
            return f"{ve}: Please Enter Word Not Character to Find Character Use find"

    def find_word(self, word: str) -> int:
        """
        methods find the word or character-first occurrence in the txt else, return -1 if not found
        @param word: str
        @return: int
        """
        return self.txt.find(word)

    def make_capital(self) -> str:
        """
        methods return the str in capital formatting
        @return: str
        """
        return self.txt.capitalize()

    def make_upper(self) -> str:
        """
        methods return the str in Upper Formatting
        @return: str
        """
        return self.txt.upper()

    def make_casefold(self) -> str:
        """
        method returns the string in lowercase, ascii and non-ascii both
        @return: str
        """
        return self.txt.casefold()

    def change_case(self) -> str:
        """
        method returns the string in swapped case
        @return: str
        """
        return self.txt.swapcase()


class ABC:

    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return f'ABC({self.msg!r})'

    def __repr__(self):
        return f'ABC({self.msg!r})'


obj = ABC("Hi")
print(obj)
print(obj.__repr__())
format_str = "{Name} was Released in 2013"
print(format_str.format(Name="GTA"))
print(format_str.format_map({"Name": "GTA V"}))


# Python program to demonstrate writing of __repr__ and
# __str__ for user defined classes

# A user defined class to represent Complex numbers
class Complex:

    # Constructor
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    # For call to repr(). Prints object's information
    def __repr__(self):
        return 'Rational(%s, %s)' % (self.real, self.imag)

    # For call to str(). Prints readable form
    def __str__(self):
        # return 'Rational(%s, %s)' % (self.real, self.imag)
        return '%s + i%s' % (self.real, self.imag)


# Driver program to test above
t = Complex(10, 20)

# Same as "print t"
print(str(t))
print(repr(t))
print("Printable: all the things are printable except escape sequence")
print('\n'.isprintable())
print(r'\n'.isprintable())
print('\\n'.isprintable())
print(f'type({5})'.isprintable())
print(" jij".isspace())
print(" ".isspace())
print("^".join(["This", "is", "Mohit"]))
print("This is Mohit".split(" "))

print("Stripping")
print('   spacious   '.lstrip())
print('www.example.com'.lstrip('w.'))
print('www.example.com'.rstrip('.omc'))
print("Difference Between Prefix and strip")
print('Arthur: three!'.lstrip('Arthur: '))
print('Arthur: three!'.removeprefix('Arthur: '))

print("Right Stripping")
print('Monty Python'.rstrip(' Python'))
print('Monty Python'.removesuffix(' Python'))
print("Mohit".ljust(100, "~"))
print("Mohit".center(100, '~'))
print("Mohit".rjust(100, "~"))
print("#".center(100, "~"))
print("IF".isidentifier())
