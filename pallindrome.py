# Program to find is string palindrome ps - can be used at Module Level
import sys

def is_palindrome(string):
    if string == "".join(list(reversed(string))):
        return True
    return False

if __name__ == "__main__":
    try:
        print(is_palindrome(sys.argv[1]))
    except:
        print(is_palindrome("naman"))
        