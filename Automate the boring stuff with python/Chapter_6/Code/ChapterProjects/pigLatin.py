#! python3
# pigLatin.py - Translates English messages into Pig Latin.

"""
Pig Latin is a language game used by English-speaking people, especially children.
The goal is to obfuscate the English language so that words are not understood by others.
To create the Pig Latin form of an English word, the initial consonant sound is transposed to
the end of the word and an ay is affixed (Ex.: "banana" would yield anana-bay).

The goal of this exercise is to write a Python program that takes a list of strings and translates
them into Pig Latin. The program should use the pyperclip module to read the text from the
clipboard and then paste the Pig Latin form to the clipboard.

This script requires the pyperclip module which must be installed first. To install it::

        pip install pyperclip
"""

print(" Welcome, Pig Latin Translator. ".center(50, "="))
print("Enter the English message: ")
message = input().split()
VOWELS = ("a", "e", "i", "o", "u", "y")
pigLatin = []
for word in message:
    # Separate the non-letters at the start of this word.
    prefixNonLetters = ""
    while len(word) > 0 and not word[0].isalpha():
        prefixNonLetters += word[0]
        word = word[1:]
    if len(word) == 0:
        pigLatin.append(prefixNonLetters)
        continue

    # Separate the non-letters at the end of the word.
    suffixNonLetter = ""
    while not word[-1].isalpha():
        suffixNonLetter += word[-1]
        word = word[:-1]

    # Remember if the word is uppercase or title case.
    wasUpper = word.isupper()
    wasTitle = word.istitle()

    word = word.lower()

    # Separate the consonant at the start of this word.
    prefixConsonants = ""
    while len(word) > 0 and not word[0] in VOWELS:
        prefixConsonants += word[0]
        word = word[1:]

    # Add the Pig Latin ending to the word.
    if prefixConsonants != "":
        word += prefixConsonants + "ay"
    else:
        word += "yay"

    # Set the word back to uppercas or title case.
    if wasUpper:
        word = word.upper()
    if wasTitle:
        word = word.title()

    # Add the non-letters back to the start or end of the word.
    pigLatin.append(prefixNonLetters + word + suffixNonLetter)


print(" ".join(pigLatin))


# example: The goal of this exercise 435 is to write a Python program.
# =============
# Output: Ethay oalgay ofyay isthay exerciseyay 435 isyay otay itewray ayay Ythonpay ogrampray.
