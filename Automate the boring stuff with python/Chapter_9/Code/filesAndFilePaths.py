# @#$^$^*&*(^&$%^#@#@%$#%$^%&*^*&)(&^&%$^@#%$#%^&*&^(&*%$^)#
#                   Files And File Paths                   #
# 1- Backslach on Windows, Forward Slach on MacOS, & Linux #
#          2- Using the / Operator to Join Paths           #
#             3- The Current Working Directory             #
#                   4- The Home Directory                  #
#              5- Absolute vs. Relative Paths              #
#  6- Creating New Folders Using the os.makedires Function #
#          7- Handling Absolute and Relative Paths         #
#            8- Getting the Parts of a File Path           #
#         9- Finding File Sizes and Folder Contents        #
#     10- Modifying a List of Files Using Glob Patterns    #
#                 11- Checking Path Validity               #
# @#$^$^*&*(^&$%^#@#@%$#%$^%&*^*&)(&^&%$^@#%$#%^&*&^(&*%$^)#

# 1- Backslach on Windows, Forward Slach on MacOS, & Linux #
from pathlib import Path

path = str(Path("spam", "bacon", "eggs"))
print(path)


My_Files = ["dataset.csv", "notebook.ipynp", "notes.txt"]
for f in My_Files:
    print(Path(r"C:\Users\MBR\Desktop", f))


#          2- Using the / Operator to Join Paths           #
from pathlib import Path

"""One of the paths must be a Path object, not a string. So we convert one of them."""

print(Path("spam") / "bacon" / "eggs")  # OUTPUT: spam\bacon\eggs
print(
    "spam" / "bacon" / "eggs"
)  # OUTPUT: TypeError: unsupported operand type(s) for /: 'str' and 'str'


#             3- The Current Working Directory             #
from pathlib import Path
import os

cwd = Path.cwd()
print(
    f"The current working directory is: {cwd}"
)  # OUTPUT:  E:\Desktop-Folders\Reading group\old version\Automate the boring stuff with python

os.chdir("C:\\Windows\\System32")  # change your working directory to another directory.
new_cwd = Path.cwd()
print(
    f"\nAfter changing the CWD, the new CWD is: {new_cwd}"
)  # OUTPUT: C:\Windows\System32


#                   4- The Home Directory                  #
from pathlib import Path
"""
The home directory is the directory that contains the user's files and folders.
On Windows, this is usually C:\Users\<username>.
On macOS and Linux, this is usually /Users/<username> or /home/<username>.
"""
home = Path.home()
print(f"Home directory: {home}")  # OUTPUT: C:\Users\MBR


#              5- Absolute vs. Relative Paths              #

"""
Absolute Path: A path that starts from the root folder.
Relative Path: A path that doesn't start from the root folder."""
relative_path = Path("Documents") / "spam" / "eggs"
absolute_path = Path.cwd() / "Documents" / "spam" / "eggs"

print(f"Relative path: {relative_path}")  # Output: Documents\spam\eggs
print(f"Absolute path: {absolute_path}")  # Output: E:\Desktop-Folders\Reading group\old version\Automate the boring stuff with python\Documents\spam\eggs
print(f"Absolute path: {absolute_path.as_posix()}")  # Output: E:/Desktop-Folders/Reading group/old version/Automate the boring stuff with python/Documents/spam/eggs
print(f"Absolute path: {absolute_path.as_uri()}")  # Output: file:///E:/Desktop-Folders/Reading%20group/old%20version/Automate%20the%20boring%20stuff%20with%20python/Documents/spam/eggs


#  6- Creating New Folders Using the os.makedires Function #
import os
os.makedirs("test/hmmm")

from pathlib import Path
Path("test/hmmm/ttt").mkdir(parents=True, exist_ok=True)


#          7- Handling Absolute and Relative Paths         #
from pathlib import Path

path = Path("spam") / "bacon" / "eggs"
print(f"is absolute path: %s" % path.is_absolute())  # OUTPUT: False

path = Path.cwd() / "test" / "hmmm" / "ttt"
print(f"is absolute path: %s" % path.is_absolute())  # OUTPUT: True


#            8- Getting the Parts of a File Path           #
from pathlib import Path
"""
C:\Users\Username\Documents\example_file.txt

Rank 0: C: (Anchor/Drive)
│
└── Rank 1: Users (Parent Directory) _______________|\\\
    └── Rank 2: Username (Parent Directory) ________|   >>>>  Path.parent
        └── Rank 3: Documents (Parent Directory) ___|///
            └── Rank 4: example_file (Name Stem)
                └── Rank 5: .txt (Suffix)
"""
path = Path(r"C:\Users\Username\Documents\example_file.txt")
print(f"Drive: {path.drive}") # OUTPUT: C:
print(f"Parent Directory: {path.parent}") # OUTPUT: WindowsPath('C:/Users/Username/Documents') 
print(f"Name Stem: {path.stem}") # OUTPUT: example_file
print(f"Suffix: {path.suffix}") # OUTPUT: .txt


#         9- Finding File Sizes and Folder Contents        #
import os
path = r"C:\Windows\System32"
os.path.getsize(path)

totalSize = 0
for fileName in os.listdir(path):
    totalSize += os.path.getsize(os.path.join(path, fileName))

print(totalSize)


#     10- Modifying a List of Files Using Glob Patterns    #
from pathlib import Path

path = Path(Path.cwd())
print(list(path.glob("*"))[-1]) # glob will take a pattern and return a list of paths that match that pattern.
path = Path(r"E:/Desktop-Folders/Reading group/old version/Automate the boring stuff with python/Chapter_1")
files = list(path.glob("*.py"))  # Get all python files in current directory
print(files[0].name) # OUTPUT: yourFirstProgram.py


#                 11- Checking Path Validity               #
from pathlib import Path

path = Path(r"C:\Windows\System32")
print(f"Path exists: {path.exists()}") # OUTPUT: True
print(f"Is it a file: {path.is_file()}") # OUTPUT: False
print(f"Is it a directory: {path.is_dir()}") # OUTPUT: True

path = Path(r"C:\Windows\System32\notExist.mo3")
print(f"Path exists: {path.exists()}") # OUTPUT: False

path = Path(r"D:")
print(f"Path exists: {path.exists()}") # OUTPUT: False

path = Path(r"E:")
print(f"Path exists: {path.exists()}") # OUTPUT: True
