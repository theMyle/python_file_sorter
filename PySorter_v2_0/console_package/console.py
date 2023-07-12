# custom package
from config_package import config
from . import functions as fn
from sort_package import sort
from sort_package import un_sort

# program flow
def start_console():
    start_app()
    start_menu()

# app startup info (ex: version, title, etc)
def start_app():
    print(f"### Welcome to {config.program_title} {config.version} By JKyle ###")
    print("The program will store the files to a folder named \"PySort_Folder\"")

# main program menu
def start_menu():
    while True:
        print("\n[-- Menu --]")
        print("Please choose an option down below: ")
        print("\t1 - Select Directory")
        print("\t2 - Exit the program")
        user_input = input(">>> ")

        if user_input == "1":
            print("\nPlease select a folder that you want the contents to be sorted ")
            print("(Do NOT select the 'PySort_Folder' if it already exists or else it will create another 'PySort_Folder' inside it)")
            input("\nPress 'Enter' to continue")
            fn.select_folder()
            sort_options()
        elif user_input == "2":
            fn.exit_program()
        else:
            print("Please select an options from the choices above.")

# sort/un_sort option menu
def sort_options():
    while True:
        print("\n[-- Sort Options --]")
        print("Please choose an option down below: ")
        print("\t1 - Sort Items")
        print("\t2 - Un_Sort Items")
        print("\t3 - Exit the program")
        user_input = input(">>> ")

        if user_input == "1":
            sort.sort_files()
        elif user_input == "2":
            un_sort.un_sort_files()
        elif user_input == "3":
                fn.exit_program()
        else:
            print("Please select an options from the choices above.")
