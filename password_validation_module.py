import re


def find_pattern(patt, text):
    m = re.search(patt, text)
    if m:
        return True
    else:
        return False


def validate(password):
    if 6 < len(password) < 13:
        if (find_pattern(r"[A-Z]", password) and
                find_pattern(r"[a-z]", password) and
                find_pattern(r"\d", password) and
                find_pattern(r"[#$%]", password)):
            return True
        else:
            return False
    else:
        return False
