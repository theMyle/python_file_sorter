from . import functions as fn
from . import sort

def start():
    print("Please choose an option down below: ")
    print("\t1 - Select Directory")
    print("\t2 - Exit the program")

    while True:
        user_input = input("> ")
        if user_input == "1":
            fn.select_folder()
            sort_options()
        elif user_input == "2":
            fn.exit_program()
        else:
            pass


def sort_options():
    while True:
        print("Please choose an option down below: ")
        print("\t1 - Sort Items")
        print("\t2 - Un_Sort Items")
        print("\t3 - Exit the program")
        user_input = input("> ")

        if user_input == "1":
            sort.sort_files()
            fn.exit_program()
        elif user_input == "2":
            #un_sort.un_sort_files()
            fn.exit_program()
        elif user_input == "3":
            fn.exit_program()
        else:
            print("Please select an options from the choices above.")