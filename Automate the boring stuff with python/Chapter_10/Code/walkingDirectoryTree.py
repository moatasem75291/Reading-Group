# @#$^$^*&*(^&$%^#@#@%$#%$^%&*^*&)(&^&%$^@#%$#%^&*&^(&*%$^)#
#                 Walking a Directory Tree                 #
# @#$^$^*&*(^&$%^#@#@%$#%$^%&*^*&)(&^&%$^@#%$#%^&*&^(&*%$^)#
"""
Say you want to rename every file in some folder and elso every file in every
subfolder of that folder. That means you need to walk through the directory tree,
starting at the top. You can do this with Python's os module, which contains a
function called os.walk(). The os.walk() function is passed a single string value:
the path of a folder. You can use os.walk() in a for loop, and it will return three
values on each iteration through the loop:
- root: A string representing the path to the folder.
- dirs: A list of the folders in the folder (excluding '.' and '..').
- files: A list of the files in the folder.
If there are subfolders, the function will also return a second tuple containing the
root, dirs, and files for that subfolder, and so on. The following program prints the
names of all the files in every folder starting at the folder path you specify.
"""

import os

TARGET_DIR = ".\\Chapter_10\\Code\\delicious"
for root, dirs, files in os.walk(TARGET_DIR):
    print(f" The Current folder is: ")
    print(f" {root} ".center(60, "-"))

    for dir in dirs:
        print(f" The subfolder of {root} is: {dir} ")

    for file in files:
        print(f" The file in {root} is: {file} ")
    print(end="\n\n\n")
