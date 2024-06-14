# Python Program to Working with Files
from check_number_input import is_number


def read_file(file_name):
    try:
        with open(file_name, "r") as f:
            print(f.read())
    except FileNotFoundError:
        print("File Not Found")


def write_file(file_name):
    with open(file_name, "a+") as f:
        file_lines = []
        print("Enter the File Content Press Enter for New Line \nps:Enter C/c to Continue\n")
        while True:
            lines = input()
            if lines.lower() == 'c':
                break
            file_lines.append(lines + "\n")
            f.writelines(file_lines)
        print(f.read())


def append_file(file_name):
    with open(file_name, "w") as f:
        file_lines = []
        print("Enter the File Content Press Enter for New Line \nps:Enter C/c to Continue\n")
        while True:
            lines = input()
            if lines.lower() == 'c':
                break
            file_lines.append(lines + "\n")
            f.writelines(file_lines)
        print(f.read())


if __name__ == "__main__":
    name = input("Enter File Name - ")
    option = input("Choose Operation\n"
                   "1- Reading\n"
                   "2- Append - \n"
                   "3- Writing  - ")
    if is_number(option):
        if option == "1":
            read_file(name)
        elif option == "2":
            append_file(name)
        elif option == "3":
            write_file(name)
