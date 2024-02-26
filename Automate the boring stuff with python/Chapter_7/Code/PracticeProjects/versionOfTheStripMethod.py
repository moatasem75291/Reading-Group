#! Python
# versionOfTheStripMethod.py - A program that replicates the strip() method of strings.
"""
Write a function that replicates the strip() method of strings. The strip() method removes
whitespace from the beginning and end of a string. If no other arguments are passed other
than the string to strip, then whitespace characters are removed from the beginning and end
of the string. Otherwise, the characters specified in the second argument to the method are
removed instead.

The function should return the modified string.
"""

import re


def version_of_strip(string: str, characters_to_remove: str = None) -> str:
    """
    Replicates the strip() method of strings.
    Args:
        string: A string to remove whitespace from.
        characters_to_remove: A string containing the characters to remove from the string.
    Returns:
        The modified string.
    """
    if characters_to_remove is None:
        return re.sub(r"^\s+|\s+$", "", string)
    else:
        return re.sub(
            f"^[{re.escape(characters_to_remove)}]+|[{re.escape(characters_to_remove)}]+$",
            "",
            string,
        )


# Test Cases:
print(version_of_strip("   Hello, World!   "))  # Expected output: "Hello, World
print(
    version_of_strip("   Hello, World!   ", "Hd!")
)  # Expected output: "   Hello, World   "
print(version_of_strip("   Hello, World!   ", "Hd! "))  # Expected output: "ello, Worl"
print(version_of_strip("   Hello, World!   ", "Hd! W"))  # Expected output: "ello, Worl"
print(version_of_strip("Hello, World!", "Hd! Wl"))  # Expected output: "ello, Wor"
