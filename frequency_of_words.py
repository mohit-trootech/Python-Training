# Python Program to find Frequency of Words
import sys
from custom_system_argument_error import ProgramNotRunFromShell

def frequency_words_whitespace_included(word):
    words_list = [i for i in word.split(" ")]
    frequency_words_dictionary = {i: words_list.count(i) for i in words_list}
    return frequency_words_dictionary


def frequency_words_whitespace_excluded(word):
    words_list = [i for i in word.split(" ") if i != ""]
    frequency_words_dictionary = {i: words_list.count(i) for i in words_list}
    return frequency_words_dictionary


if __name__ == "__main__":
    try:
        print(frequency_words_whitespace_excluded(sys.argv[1]))
        print(frequency_words_whitespace_included(sys.argv[1]))
    except:
        user_input = input("Enter Anything String - ")
        print(f"without Extra Whitespace - {frequency_words_whitespace_excluded(user_input)}")
        print(f"with Extra Whitespace - {frequency_words_whitespace_included(user_input)}")
