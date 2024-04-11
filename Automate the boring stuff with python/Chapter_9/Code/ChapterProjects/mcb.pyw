#! Python
# mcb.byw - Saves and loads pieces of text to the clipboard.
# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
#        py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
#        py.exe mcb.pyw list - Loads all keywords to clipboard.
import shelve, sys, pyperclip

mcbFile = shelve.open("mcb")
args = sys.argv

# Save Clipboard content.
if len(args) == 3 and args[1].lower() == "save":
    keyWord = args[2]
    mcbFile[keyWord] = pyperclip.paste()

elif len(args) == 2:
    # List keywords and load content.
    if args[1].lower() == "list":
        keyWords = str(list(mcbFile.keys()))
        pyperclip.copy(keyWords)

    elif args[1] in mcbFile:
        pyperclip.copy(mcbFile[args[1]])

mcbFile.close()
