#! Python
# mcb.byw - Saves and loads pieces of text to the clipboard.
# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
#        py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
#        py.exe mcb.pyw list - Loads all keywords to clipboard.
#        py.exe mcb.pyw delete <keyword> - Deletes keyword from database.
#        py.exe mcb.pyw delete - Deletes all keywords from database.

import shelve, sys, pyperclip

mcbFile = shelve.open("mcb")
args = sys.argv

# Save Clipboard content.
if len(args) == 3 and args[1].lower() == "save":
    keyWord = args[2]
    mcbFile[keyWord] = pyperclip.paste()

elif len(args) == 3 and args[1].lower() == "delete":
    keyWord = args[2]
    if keyWord in mcbFile:
        del mcbFile[keyWord]
    else:
        print(f"Keyword '{keyWord}' does not exist in the database.")

elif len(args) == 2:
    # List keywords and load content.
    if args[1].lower() == "list":
        keyWords = str(list(mcbFile.keys()))
        pyperclip.copy(keyWords)

    elif args[1].lower() == "dleete":
        for key in mcbFile.keys():
            del mcbFile[key]
    elif args[1] in mcbFile:
        pyperclip.copy(mcbFile[args[1]])

mcbFile.close()
