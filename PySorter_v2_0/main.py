# PySorter v2.0
# Created by John Kyle J. Desamparo     Date: 3/07/2023

# [--- Notes ---]
# [ Hi! This is a hobby project of mine, the PySorter. Feel free to re-use or change the code to your liking ]
# [ If you have any comments, issues, or suggestions feel free to reach out. --------------------------------]
# [ You can contact me via Twitter: @Benf_105 ---------------------------------------------------------------]

# [--- What is PySorter ---]
# [ PySorter is a tool I made to clean, fix, and organize my files. Sometimes when I download or transfer ---]
# [ lots and lots of files and I sometimes forget organizing them so why not automate it using python. ------]

# [--- How it Works---]
# [ 1. You choose a directory/folder that you want to be sorted ------------------------------------------------------------]
# [ 2. Scans the files in that directory and stores what type of files are there. ------------------------------------------]
# [ 3. It then creates a folder named "PySorter" which will be used to store the files. ------------------------------------]
# [ 4. Next, it creates sub folders for each file extensions identified so there will be one for .docx and .pdf for example.]
# [ 5. Finally, the program moves the files to each of their respective folder accordingly. --------------------------------]

# importing packages
import console_package as cp
import sort_package as sp

# main function
def Main():
    cp.start_console
