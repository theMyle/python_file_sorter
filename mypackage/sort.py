import os
import shutil

pysort = "Pysort_folder"

def sort_files():
    try:
        os.mkdir(pysort)
        print("\nCreated a Pysort folder")
    except FileExistsError:
        print("\nUsing an existing Pysort folder ")
        pass

    files = get_files()                                 # returns a list
    file_extensions = get_extensions(files)             # returns a list
    sub_folders = create_sub_folders(file_extensions)   # returns a list

    print(f"folders: {sub_folders}\n")

    for fname in files:
        ext = os.path.splitext(os.path.join(os.getcwd(), fname))[-1]
        for folder in sub_folders:
            if ext == folder:
                try:
                    filepath = os.path.join(os.getcwd(), fname)
                    dest = os.path.join(os.getcwd(), pysort, folder)
                    shutil.move(filepath, dest)
                    print(f"{fname} | moved to -> {folder} ")
                except FileExistsError as fe:
                    print(f"already exists: {fname}")
    
    print("\nOperation Complete!")


def get_files():
    dir = os.listdir(os.getcwd())
    files = [i for i in dir if os.path.isfile(os.path.join(os.getcwd(), i))] 
    return files


def get_extensions(files):
    list = []
    for items in files:
        file_name = os.path.splitext(items)
        extension = file_name[-1]
        if extension not in list:
            list.append(extension)
    return list


def create_sub_folders(list):
    ls = []

    for item in list:
        try:
            os.mkdir(os.path.join(os.getcwd(), pysort, item))
            ls.append(item)
            print(f"{item} sub folder created")
        except FileExistsError as fe:
            print(f"using an existing {item} folder")
        except FileNotFoundError as fnf:
            print(f"folder not found")

    # check for existing sub folders
    old = os.listdir(os.path.join(os.getcwd(), pysort))
    for i in old:
        ls.append(i)

    return ls
