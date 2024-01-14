import functions
import os
import shutil


def sort_files():

    try:
        os.mkdir("Pysort_Folder")
        print("Created a Pysort folder")
    except FileExistsError:
        print("Using an existing Pysort folder ")
        pass

    files = get_files()
    extensions = get_extensions()

    fileExtensions = get_list_of_extensions(listOfFiles)

    sub_folders = create_sub_folders(fileExtensions)

    move_items(extension=fileExtensions, file_names=listOfFiles)

    functions.exit_program()

    return 0


def get_files():
    list_of_files = os.listdir(os.getcwd())
    # exclude folders
    list_of_files = [i for i in list_of_files if os.path.isfile(os.path.join(os.getcwd(), i))] 
    print(f"\nList of files:\n{list_of_files}")
    return list_of_files


def create_folder():
    active_folder_path = os.getcwd()
    active_folder_name = active_folder_path.split("\\")[-1]
    # Checks if the user is already in the PySort Folder
    if (active_folder_name == config.folder_name):
        print("\nAlready in the PySort Folder")
    else:
        try:
            # Create a folder in the current directory
            os.mkdir(config.folder_name)
            print(f"\nCreated a new {config.folder_name}")
        except FileExistsError:
            pass
        return 0


def move_to_folder():
    PySort_folder_path = os.path.join(os.getcwd(), config.folder_name)
    try:
        os.chdir(PySort_folder_path)
    except FileExistsError:
        os.chdir(PySort_folder_path)
        print(f"\nUsing an existing {config.folder_name}")
    return 0 


def get_extensions(files):
    list = []
    for items in files:
        file_name = os.path.splitext(items)
        extension = file_name[-1]
        
        if extension not in list:
            list.append(extension)

    return list


def create_sub_folders(folder_names):
    """Creating sub folders for each unique file"""
    for item in folder_names:
        try:
            folder_path = os.path.join(os.getcwd(), item)
            os.mkdir(folder_path)
            print(f"{item} sub folder created")
        except FileExistsError as fe:
            print(f"{item} sub folder already exists")
        except FileNotFoundError as fnf:
            pass  # directory doesn't exists
    return 0


def move_items(extension, file_names):
    """Move items"""
    print(" ")
    base_path = os.path.dirname(os.getcwd())
    for item in extension:
        folder_path = os.path.join(os.getcwd(), item)
        for names in file_names:
            # get the file extension from the file name
            ext = os.path.splitext(names)[-1]
            # if file extension is similar to the folder name then move the file to the folder
            if item == ext:
                try:
                    # (file path, destination)
                    shutil.move(os.path.join(base_path, names), rf"{folder_path}")
                    print(f"Successfully Moved - [{names}]")
                except FileExistsError as fe:
                    print(f"FILE ALREADY EXISTS: [{names}]. Skipping...")

    print("\n[ Operation Complete ]")
    return 0
