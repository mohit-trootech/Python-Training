import re

print("""
Following are the criteria for the password:
1. At least 1 letter between [a-z]
2. At least 1 number between [0-9]
1. At least 1 letter between [A-Z]
3. At least 1 character from [$#@]
4. Minimum length of transaction password: 6
5. Maximum length of transaction password: 12
""")


def find_pattern(patt, text):
    m = re.search(patt, text)
    if m:
        return True
    else:
        return False


password = input("Enter the Password of Following Criteria - ")

if 6 < len(password) < 13:
    if (find_pattern(r"[A-Z]", password) and
            find_pattern(r"[a-z]", password) and
            find_pattern(r"\d", password) and
            find_pattern(r"[$#A]", password)):
        print("Password Validated Successfully")
    else:
        print("Password Validation Failed Try Again with given Criteria")
else:
    print("Password Length should between 6 - 12")
