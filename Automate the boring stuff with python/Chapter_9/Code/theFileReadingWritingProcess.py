# @#$^$^*&*(^&$%^#@#@%$#%$^%&*^*&)(&^&%$^@#%$#%^&*&^(&*%$^)#
#            The File Reading / Writing Process            #
#         1- Opening Files with the open() Function        #
#             2- Reading The Contents of Files             #
#                    3- Writing to Files                   #
# @#$^$^*&*(^&$%^#@#@%$#%$^%&*^*&)(&^&%$^@#%$#%^&*&^(&*%$^)#

import os
from pathlib import Path

CWD = Path(Path.cwd(), "Chapter_9\\Code")
os.chdir(CWD)
path = Path("spam.txt")
path.write_text("Hello, world")

path.read_text()  # 'Hello, world'


#         1- Opening Files with the open() Function        #
helloFile = open("spam.txt")


#             2- Reading The Contents of Files             #
helloContent = helloFile.read()
helloContent  # 'Hello, world'

poemFile = open("poem.txt")
poemContent = poemFile.readlines()
poemContent  # ['Roses are red,\n', 'Violets are blue,\n', 'Coding is fun,\n', 'And so are you!']
poemFile.close()


#                    3- Writing to Files                   #

poemFile = open("poem.txt", "w")
poemFile.write("Roses are red,\nViolets are blue,\n")
poemFile.close()

appendFile = open("poem.txt", "a")
appendFile.write("\nCoding is fun,\nAnd so are you!")
appendFile.close()
