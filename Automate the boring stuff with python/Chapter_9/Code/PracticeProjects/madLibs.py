#! python3
# madLibs.py - Reads in text files and lets the user add their own text anywhere the word ADJECTIVE, NOUN, ADVERB, or VERB appears in the text file.
from string import Template

ADJECTIVE = ...
NOUN1 = ...
VERB = ...
NOUN2 = ...

while True:
    print("Enter an adjective:")
    ADJECTIVE = input()
    print("Enter a noun:")
    NOUN1 = input()
    print("Enter a verb:")
    VERB = input()
    print("Enter a noun:")
    NOUN2 = input()

    with open("Chapter_9/Code/PracticeProjects/mad_libs.txt") as f:
        """search for each word and replace it with the user's input, using Regex."""
        content = f.readlines()
        content = " ".join(content)
        MADLIBS_TEMPLATE = Template(content)
        text = MADLIBS_TEMPLATE.substitute(
            ADJECTIVE=ADJECTIVE, NOUN1=NOUN1, VERB=VERB, NOUN2=NOUN2
        )

    print(text, end="\n\n\n")
    print("Would you like to play again? (yes or no)")
    playAgain = input()
    if playAgain != "yes":
        break
