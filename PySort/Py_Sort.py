import os
import sys

# variables
folder_name = "PySort_Folder"
current_directory = os.getcwd()
"C:\Programming\Python\Projects\Ongoing\Python_File_Sortinator_(PySort)\Test Folder\New Microsoft Excel Worksheet.xlsx"
# functions
def print_directory():
    print(f"Current Working Directory: {os.getcwd()}\n")

def change_directory():
    print(f"\n[-- Change Directory --]\nPlease copy and enter the new path to the desired folder you want to be sorted. \nYou can use the command (ctrl + shift + v) to paste. \n")
    path = input(r">>> ")
    if (os.getcwd() == path):
        print("\n--- You are already in this directory ---\n")
        return 0
    try:
        current_directory = os.chdir(path)
        print(f"\nSuccess! Working directory successfully changed")
        print_directory()
        return 0
    except OSError as e:
        print(f"\nAn OS error occured: {e}")
        input("\nPlease double check your folder path and make sure it\'s the right one and try again.\n -- Press ENTER to Continue --")
        change_directory()
    
def sort_items():
    try:
        os.mkdir(folder_name)
        os.chdir(fr"{os.getcwd()}\{folder_name}")
        print(f"\nCreated a new {folder_name}: {os.getcwd()}")
    except FileExistsError as e:
        os.chdir(fr"{os.getcwd()}\{folder_name}")
        print(f"\nUsing an existing {folder_name}: {os.getcwd()}")

# Startup Prompts
print("### Welcome PySorter v1.0 By JKyle ###")
print_directory()

# Asks for user inputs
user_prompt = input("Please choose an option down below (1 or 2): \n\t1 - Sort current directory \n\t2 - Change directory\n>>> ")

# Uses a while loop to make sure to only take the desired inputs
while True:
    if (user_prompt == "1"):
        print("[-- Sort --]")
        user_prompt = input(f"Sort current Directory? (Y/n): ")
        if (user_prompt in ["y", "Y"]):
            sort_items()
            break
        if (user_prompt in ["n", "N"]):
            continue
        else:
            user_prompt = input(f"\nSort current Directory? (Y/n): ")

    # Change Directory
    if (user_prompt == "2"):
        change_directory()
        user_prompt = "1"

    # Loop
    else:
        print("\nPlease enter a number (1 or 2):")
        user_prompt = input("\t1 - Sort current directory \n\t2 - Change directory\n>>> ")
        


