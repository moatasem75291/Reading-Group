# @#$^$^*&*(^&$%^#@#@%$#%$^%&*^*&)(&^&%$^@#%$#%^&*&^(&*%$^)#
#                     The shutil Module                    #
#               1- Copying Files and Folders               #
#         2- Moving and Renaming Files and Floders         #
#        3- Permanentaly Deleting Files and Folders        #
#        4- Safe Deletes with the send2trach Module        #
# @#$^$^*&*(^&$%^#@#@%$#%$^%&*^*&)(&^&%$^@#%$#%^&*&^(&*%$^)#

#               1- Copying Files and Folders               #
import shutil
from pathlib import Path

source = Path(Path.cwd(), r"Chapter_9\Code\spam.txt")
destination = Path(Path.cwd(), r"Chapter_10\Code")
result = shutil.copy(source, destination)  # Copy the file to the destination folder
print("Result of copying (Path Return): ", result)

#         2- Moving and Renaming Files and Floders         #
import shutil
from pathlib import Path

source = Path(Path.cwd(), r"Chapter_9\Code\poem.txt")
destination = Path(Path.cwd(), r"Chapter_10\Code")
shutil.move(source, destination)  # Move the file to the destination folder


#        3- Permanentaly Deleting Files and Folders        #
""" Delete files and folders permanently. 
    Be careful when using this function. 
    It will delete the file or folder permanently. 
    There is no way to recover the file or folder. 
    Use it with caution. 
    
    os.unlink(source)  # Delete the file permanently 
    os.rmdir(Path)  # Delete the folder permanently, but only if it is empty 
    shutil.rmtree(Path) # Delete the folder permanently  along with all its contents
"""

#        4- Safe Deletes with the send2trach Module        #
import send2trash

baconFile = open(".\\Chapter_10\\Code\\bacon.txt", "a")
baconFile.write("Bacon is not a vegetable.")

baconFile.close()
send2trash.send2trash(".\\Chapter_10\\Code\\bacon.txt")
