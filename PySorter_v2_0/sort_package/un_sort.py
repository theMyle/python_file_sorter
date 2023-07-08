from config_package import config
from console_package import functions

import sys
import os
import shutil


def un_sort_files():
    """main UnSort function logic"""
    base_path = check_PySort_dir()
    move_items(base_path)
    clear_empty_folder()
    functions.exit_program()


def check_PySort_dir():
    """Checks if you are inside the PySort folder"""
    active_folder_path = os.getcwd()
    active_folder_name = active_folder_path.split("\\")[-1]
    if (active_folder_name == config.folder_name):
        base_path = os.path.dirname(os.getcwd())
        return base_path # already in the pysort folder
    else:
        active_folder_content = os.listdir(active_folder_path)
        pysort_path = os.path.join(active_folder_path, config.folder_name)
        if (config.folder_name in active_folder_content) and (os.path.isdir(pysort_path)):
            # if pysort folder in current dir, move inside it.
            os.chdir(pysort_path)
            base_path = os.path.dirname(pysort_path)
            return base_path
        else:
            # if pysort folder in non-existent, set current dir as base
            base_path = os.getcwd()
            return base_path
    

def move_items(arg):
    base_path = arg
    folders_list = os.listdir(os.getcwd())
    success = 0
    failed = 0
    print("")

    for i in folders_list:
        folder_path = os.path.join(os.getcwd(), i)
        items_list = os.listdir(folder_path)
        for x in items_list:
            file_path = os.path.join(folder_path, x)
            try:
                # (filepath, destination)
                shutil.move(file_path, base_path)
                success += 1
                print(f"Successfully Moved - [{x}]")
            except FileExistsError:
                print(f"A FILE WITH THE NAME [\"{x}\"] ALREADY EXISTS. Skipping...")
    
    if success > 0:
        print(f"\n[ A total of {success} (SUCCESS) files were moved outside ]")
    if failed > 0:
        print(f"[ A total of {failed} (FAILED) files remained inside the PySort_Folder ]")
    return 0


def clear_empty_folder():
    folder_list = os.listdir(os.getcwd())
    for folder in folder_list:
        folder_path = os.path.join(os.getcwd(), folder)
        if (os.listdir(folder_path) == []):
            os.rmdir(folder_path)
    return 0