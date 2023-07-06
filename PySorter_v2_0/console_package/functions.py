# imports
import tkinter as tk
from tkinter import filedialog
from ctypes import windll
import os
import sys

def exit_program():
    print("\nThanks for using the app!")
    input("\n--- Press Enter to close the program ---")
    sys.exit()

def select_folder():
    windll.shcore.SetProcessDpiAwareness(1) # Fixes DPI in windows
    root = tk.Tk()                          # Create a Tkinter root window
    root.withdraw()
    root.attributes("-topmost", True)       # Set the window attributes to be "topmost"
    path = filedialog.askdirectory()        # Sets the path to the selected folder

    folder = path.split("/")
    folder = folder[-1]
    print(f'\n{folder} folder selected')

    os.chdir(f"{path}")                    # Change directory to the new path

