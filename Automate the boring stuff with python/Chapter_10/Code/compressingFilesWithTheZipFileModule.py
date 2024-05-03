# @#$^$^*&*(^&$%^#@#@%$#%$^%&*^*&)(&^&%$^@#%$#%^&*&^(&*%$^)#
#         Compressing Files with the zipfile Module        #
#                   1- Reading ZIP Files                   #
#               2- Extracting from ZIP Files               #
#            3- Creating and Adding to ZIP Files           #
# @#$^$^*&*(^&$%^#@#@%$#%$^%&*^*&)(&^&%$^@#%$#%^&*&^(&*%$^)#

#                   1- Reading ZIP Files                   #
import zipfile, os
from pathlib import Path

home = Path.cwd() / "Chapter_10\\Code\\"
exampleZip = zipfile.ZipFile(home / "example.zip")
exampleZip.namelist()  # OUTPUT: ['compressingFilesWithTheZipFileModule.py', 'delicious/cats/catNames.txt', 'delicious/cats/zophie.jpg', 'delicious/spam.txt', 'delicious/walnut/butter.txt', 'spam.txt']

exampleInfo = exampleZip.getinfo("compressingFilesWithTheZipFileModule.py")
print(
    f"Compressed file is {round(exampleInfo.file_size / exampleInfo.compress_size, 2)}x smaller!!"
)
exampleZip.close()


#               2- Extracting from ZIP Files               #
import zipfile, os
from pathlib import Path

p = Path.cwd() / "Chapter_10\\Code\\"
z_opject = zipfile.ZipFile(p / "example.zip")
z_opject.extractall(p / "decompress")
z_opject.close()


#            3- Creating and Adding to ZIP Files           #
import zipfile
from pathlib import Path

p = Path.cwd() / "Chapter_10\\Code\\"
new_zip = zipfile.ZipFile(p / "new_zipFile.zip", "w")
new_zip.write(p / "spam.txt", compress_type=zipfile.ZIP_DEFLATED)
new_zip.close()
