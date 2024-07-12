# Sample python code for the usage of pathlib module provided by the python

import pathlib
import sys


class FunctionalitiesOfPathlib:

    def __init__(self):
        pass

    def list_all_subdirectories_in_a_directory(self, path_of_main_directory):
        path_object = pathlib.Path(path_of_main_directory)
        for item in path_object.iterdir():
            if item.is_dir():
                print(item)

    def list_all_files_in_a_directory(self, path_of_main_directory):
        path_object = pathlib.Path(path_of_main_directory)
        for item in path_object.iterdir():
            if not item.is_dir():
                print(item)

    def check_file_present(self, path_to_file):
        path_object = pathlib.Path(path_to_file)
        if path_object.is_file():
            print("File is present.")
            return True
        else:
            print("File is not present.")
            return False

    def get_current_working_directory(self):
        code_cwd = pathlib.Path().cwd()
        print("The current working directory is: {}".format(code_cwd))

    def change_current_working_directory(self, path_to_new_directory):
        code_cwd = pathlib.Path().cwd()
        path_object = pathlib.Path(path_to_new_directory)
        return_code = path_object.cd()
        if return_code:
            print(
                "The Current working directory changed successfully from {} to {}".format(
                    code_cwd, path_to_new_directory
                )
            )
            return True
        else:
            print("Unable to change the current working directory.")
            return False


def main():

    #
    while True:
        print("Please choose one of the appropriate options::")
        print("1. To print all the sub-directories of a folder/dir.")
        print("2. To print all the files present inside a folder/directory.")
        print("3. Check the existence of a specified file")
        print("4. To check the current directory of the code execution.")
        print(
            "5. To modify the current directory of the code execution. (using the chdir() function)"
        )
        print("6. To exit from the code execution.")
        menu_choice = input()
        menu_choice = int(menu_choice)

        pathlib_object = FunctionalitiesOfPathlib()

        if menu_choice == 1:
            print(
                ">Enter the absolute path of the directory whose sub-directories you want to list::"
            )
            input_str = input()
            pathlib_object.list_all_subdirectories_in_a_directory(input_str)

        elif menu_choice == 2:
            print(
                ">Enter the absolute path of the directory whose files you want to list::"
            )
            input_str = input()
            pathlib_object.list_all_files_in_a_directory(input_str)

        elif menu_choice == 3:
            print(
                ">Enter the absolute path of the file which you want to check is present::"
            )
            input_str = input()
            pathlib_object.check_file_present(input_str)

<<<<<<< HEAD
=======
            # on selecting the  fourth option the current working directory of the code is printed
>>>>>>> 0ffce43 ([Pathlib])
        elif menu_choice == 4:
            pathlib_object.get_current_working_directory()

        elif menu_choice == 5:
            print(
                ">Enter the absolute path to the new directory to which you want to change::"
            )
            input_str = input()
            pathlib_object.change_current_working_directory(input_str)

        print("Do you want to continue or exit the code execution?[y/n]")
        continue_or_exit = input()

        if continue_or_exit == "y" or continue_or_exit == "Y":
            pass
        elif continue_or_exit == "n" or continue_or_exit == "N":
            return


if __name__ == "__main__":
    main()
