from cx_Freeze import setup, Executable

# Specify the list of scripts or modules you want to convert to executables
executables = [
    Executable("main.py")
]

# Define additional options for the setup
options = {
    'build_exe': {
        'packages': ["config_package", "sort_package", "console_package"],  # List of packages to include
        'include_files': []  # List of additional files to include
    }
}

# Run the setup
setup(
    name="PySorter",
    version="2.0",
    description="Python File Sorter!",
    executables=executables,
    options=options
)
