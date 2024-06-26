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
        return "Hello"

    def __repr__(self):
        return f'ABC({self.msg!r}'


obj = ABC("Hi")
print(obj)
print(obj.__repr__())
