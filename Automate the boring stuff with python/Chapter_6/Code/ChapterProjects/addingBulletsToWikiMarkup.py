#! python3
# addingBulletsToWikiMarkup.py - Adds Wikipedia bullet points to the start
# of each line of text on the clipboard.

"""
When editing a Wikipedia article, you can create a bulleted list by putting each list item
on its own line and placing a star in front. But say you have a really large list that you want to
add bullet points to. You could just type those stars at the beginning of each line, one by one.
Or you could write a simple program that does this for you.

The goal of this exercise is to write a Python program that
takes a list of strings and adds a star and space to the beginning of each string. The program
should use the pyperclip module to read the list from the clipboard and then paste the new list
to the clipboard.

Here's what the program does:
1. Paste text from the clipboard.
2. Do something to it.
3. Copy the new text to the clipboard.
This script requires the pyperclip module which must be installed first. To install it::
    
        pip install pyperclip

"""

import pyperclip

text = pyperclip.paste()

lines = text.split("\n")
lines = ["* " + line.title() for line in lines]

text = "\n".join(lines)
pyperclip.copy(text)
print("The text has been copied to the clipboard.")
