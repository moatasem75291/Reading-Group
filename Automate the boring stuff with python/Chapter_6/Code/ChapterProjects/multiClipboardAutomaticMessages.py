#! python3
# multiClipboardAutomaticMessages.py - A multi-clipboard program that stores text.
"""
Extend the multi-clipboard program in this chapter so that it has a key-value pair feature. 
This would allow you to assign a key, such as 'pycon2019',
and have the clipboard text be associated with that key.
You can then use the key to retrieve the associated text later on.
This way, you can have a sort of multi-clipboard that you can access with just a few keystrokes.

This is what your program does:
- The command line argument for the key is checked.
- If the key is found, the text is copied to the clipboard.
- If the key is not found, the program prints an error message and exits.
- This means your program will need to use the sys.argv list to read the command line arguments.
- You will also need to read and write to the clipboard.

"""
import sys
import pyperclip

# Dictionary of key-value pairs
CLIPBOARD = {
    "agree": "Yes, I agree. That sounds fine to me.",
    "busy": "Sorry, can we do this later this week or next week?",
    "cancel": "No problem, I'll cancel my order.",
    "confirm": "Yes, I confirm my order.",
    "hello": "Hello, how are you?",
}


def main():
    if len(sys.argv) < 2:
        print(
            "Usage: python multiClipboardAutomaticMessages.py [key] - copy key's value to clipboard",
            sys.argv,
            sep="\n",
        )
        sys.exit()

    key = sys.argv[1]
    if key in CLIPBOARD:
        pyperclip.copy(CLIPBOARD[key])
        print(
            f"Text for {key} copied to clipboard.",
            sys.argv,
            sep="\n",
        )
    else:
        print(f"There is no text for {key}.")
        sys.exit()


if __name__ == "__main__":
    main()
