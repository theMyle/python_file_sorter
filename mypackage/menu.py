from . import functions as fn

def start():
    while True:
        print("\n[-- Menu --]")
        print("Please choose an option down below: ")
        print("\t1 - Select Directory")
        print("\t2 - Exit the program")
        user_input = input("> ")

        if user_input == "1":
            fn.select_folder()
            sort_options()
            pass
        elif user_input == "2":
            fn.exit_program()
            pass
        else:
            print("Please select an options from the choices above.")


def sort_options():
    while True:
        print("\n[-- Sort Options --]")
        print("Please choose an option down below: ")
        print("\t1 - Sort Items")
        print("\t2 - Un_Sort Items")
        print("\t3 - Exit the program")
        user_input = input(">>> ")

        if user_input == "1":
            #sort.sort_files()
            pass
        elif user_input == "2":
            #un_sort.un_sort_files()
            pass
        elif user_input == "3":
            fn.exit_program()
        else:
            print("Please select an options from the choices above.")