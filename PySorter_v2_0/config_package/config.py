import os
import json

# set config json's file path
file_name = "config.json"
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, file_name)

# read the config file
with open(file_path, "r") as f:
    data = json.load(f)

# program variables
program_title = data["Settings"]["program_title"]
version = data["Settings"]["version"]
folder_name = data["Settings"]["folder_name"]
current_directory = os.getcwd()
