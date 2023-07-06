# PySorter v1.0
# Created by John Kyle J. Desamparo     Date: 13/06/2023

# [--- Notes ---]
# [ Hi! This is a hobby project of mine, the PySorter. Feel free to re-use or change the code to your liking ]
# [ If you have any comments, issues, or suggestions feel free to reach out. --------------------------------]
# [ You can contact me via Gmail: jangkayld@gmail.com. || or Twitter: @Benf_105------------------------------]

# [--- What is PySorter ---]
# [ PySorter is a tool I made to clean, fix, and organize my files. Sometimes when I download or transfer ---]
# [ lots and lots of files and I sometimes forget organizing them so why not automate it using python. ------]

# [--- How it Works---]
# [ 1. First, by choosing a directory where you want files to be sorted. ---------------------------------------------------]
# [ 2. Scans the files in that directory and stores what type of files are there. ------------------------------------------]
# [ 3. It then creates a folder named "PySorter" which will be used to store the files. ------------------------------------]
# [ 4. Next, it creates sub folders for each file extensions identified so there will be one for .docx and .pdf for example.]
# [ 5. Finally, the program moves the files to each of their respective folder accordingly. --------------------------------]

# Imports
import subprocess
import os
import sys
import re
import shutil
import tkinter as tk
from tkinter import filedialog
from ctypes import windll

# Program Variables
program_title = "PySorter"
version = "v1.0"
folder_name = "PySort_Folder"
packages = []
default_directory = os.getcwd()

# [ ----- Function Definitions ----- ]
# Starts the program and download the necessary files
def start_app():
    print(f"### Welcome to {program_title} {version} By JKyle ###")
    print("The program will store the files to a folder named \"PySort_Folder\"")
    print_directory()
    install_packages(packages)

# [--- Program Menu ---]
def start_main_menu():
    while True:
        user_prompt = menu_prompt()
        if user_prompt == "1":
            sort_option()
        if user_prompt == "2":
            change_directory_option()
            sort_option()
        if user_prompt == "3":
            quit_option()

# [-- File Sorting Function --]
def sort_items():
    create_folder()

# [-- Change Directory Option and Function --]
def change_directory_option():
    global default_directory

    print(f"\n[--- Change Directory Option ---]")
    print(f"Please copy and enter the path of desired folder.")
    print(f"Example: Paste - [ C:\\Users\\[YourUsername]\\Downloads ] - To select the Downloads folder. ")
    print(f"\n\t* You can use the command (ctrl + shift + v) to paste. ")
    print(f"\nOptions:")
    print(f"\t1 - Open a folder selection window")
    print(f"\t2 - Exit the program")
    path = input(r">>> ")                       # User Input

    if (os.getcwd() == path):
        print("\n--- You are already in this directory ---")

    if (path == "1"):                           # Opens a Folder selection window
        windll.shcore.SetProcessDpiAwareness(1) # Fixes DPI in windows
        root = tk.Tk()                          # Create a Tkinter root window
        root.withdraw()
        root.attributes("-topmost", True)       # Set the window attributes to be "topmost"
        path = filedialog.askdirectory()        # Sets the path to the selected folder

    if (path == "!quit"):                       # Quit Command
        quit_option()

    try:
        os.chdir(f"{path}")                    # Change directory to the new path
        default_directory = path
        print(f"\n[-- Success! Working directory successfully changed --]")
        print_directory()
    except OSError as e:
        print(f"\nAn OS error occured: {e}")
        print("\nPlease double check your folder path and make sure it\'s the right one and try again.")
        input("-- Press ENTER to Continue --")
        change_directory()

# [-- Quit Function --]
def quit_option():
    input("\n--- Press Enter to close the program ---")
    sys.exit()

# [-- Print Current Directory Function --]
def print_directory():
    print(f"Current Directory -->: {os.getcwd()}")

# Creates a custom folder
def create_folder():
    global pysort_folder_path
    try:
        # Create a folder change it as the current directory
        os.mkdir(folder_name)
        os.chdir(fr"{os.getcwd()}\{folder_name}")
        pysort_folder_path = os.getcwd()
        print(f"\nCreated a new {folder_name}: {os.getcwd()}")
    except FileExistsError as e:
        # Uses existing folder if there's any
        os.chdir(fr"{os.getcwd()}\{folder_name}")
        pysort_folder_path = os.getcwd()
        print(f"\nUsing an existing {folder_name}: {os.getcwd()}")

# Program Menu
def menu_prompt():
    print("\n[-- Menu --]")
    print("Please choose an option down below: ")
    print("\t1 - Sort items in current directory")
    print("\t2 - Change directory")
    print("\t3 - Exit the program")
    user_prompt = input(">>> ")
    return user_prompt

# Sort Menu Option
def sort_option():
    while True:
        print("\n[--- Sort Option ---]")
        print_directory()
        print("\nSort Current Directory?")
        print("\t1 - Yes")
        print("\t2 - No")
        user_prompt = input(">>> ")
        if user_prompt in ["1", "y"]:
            user_prompt = input("\nAre you sure? (Y/n): ")
            if user_prompt in ["1", "y", 'Y']:
                sort_items()
                print("\n+++ Files succesfully sorted! +++")
                quit_option()
            if user_prompt in ["n", "2", "N"]:
                quit_option()
            else:
                user_prompt = input("Are you sure? (Y/n)")
                continue
        if user_prompt in ["n", "2"]:
            break
        else:
            print(f"Dir: {os.getcwd()}")
            user_prompt = input(f"Sort current Directory? (Y/n): ")

# Package Installation
def install_packages(packages_used):
    if (len(packages_used) == 0):
        return
    else:
        print("\n--- Installing Required Packages ---")
        print(f"Packages: {packages_used}")

        # runs pip install [package name list] to install packages inside the list
        for package in packages_used:
            result = subprocess.run(['pip', 'install', package], capture_output=True, text=True)
            if "Requirement already satisfied" not in result.stdout:
                print(f"{package}: Successfully installed")
            else:
                print(f"{package}: already installed")

# Get file extension function with regex
# can also be done with os.path.splitext()
def get_file_extensions():
    file_extensions = []
    for item in list_of_files:
        # captures a string starting with "." including any combination of letters after it
        extension = re.search(r'\.(\w+)$', item)
        if extension:
            if extension.group(1) in file_extensions:
                continue
            else:
                file_extensions.append(extension.group(1))
    print("\nFile extensions status: \tAcquired")
    return file_extensions

# Get file names
def get_file_names():
    file_names = []
    for item in list_of_files:
        if item == program_file_name:
            continue
        else:
            file_names.append(item)
    print("File names status: \t\tAcquired")
    return file_names

# Create sub-folders
def create_sub_folders():
    print("\n[-- Creating sub folders --]")
    for extension in file_extensions:
        try:
            os.mkdir(fr"{os.getcwd()}\{extension}")
            print(f"\t{extension}: \tFolder created")
        except:
            print(f"\t{extension}: \tFolder already exists")
    sub_folders = file_extensions
    return sub_folders
            
# Move items to their respective folders
def move_items():
    print("\nFiles Moved:")
    # get the path for the folder created (ex: pdf [folder])
    for file_extensions in sub_folders:
        path = fr"{os.getcwd()}\{file_extensions}"
        for files in list_of_files:
            # secures the match to only move the desired files
            match_extension = f".{file_extensions}"
            if match_extension in files:
                try:
                    shutil.move(f"{default_directory}\\{files}", fr"{path}")
                    print(f"{files} - {path}")
                except:
                    print(f"{files} - [A File with the same name already exists]")

# [--- Sort Items Function ---]
def sort_items():
    global program_file_name
    global list_of_files
    global file_extensions
    global file_names
    global sub_folders

    program_file_name = os.path.basename(__file__)
    list_of_files = os.listdir(os.getcwd())
    create_folder()
    file_extensions = get_file_extensions()
    file_names = get_file_names()
    sub_folders = create_sub_folders()
    move_items()

# [ ---- Program Flow ---- ]
start_app()             # Starts the program
start_main_menu()       # Loads the menu

