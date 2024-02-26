#! Python
# strongPasswordDetection.py - A program that uses regular expressions to make sure
# the password string it is passed is strong.
"""
Write a function that uses regular expressions to make sure the password string it is passed is strong.
A strong password is defined as one that is at least eight characters long,
contains both uppercase and lowercase characters, and has at least one digit.
You may need to test the string against multiple regex patterns to validate its strength.

The function should return True if the password is strongand False if it is not.


A strong password is defined as follows:
- At least eight characters long
- Contains both uppercase and lowercase characters
- Has at least one digit
- Has at least one special character (either !, @, #, $, %, ^, &, or *)
"""

import re


def is_strong_password(password: str):
    """
    Checks if the given password is strong.
    Args:
        password: A string representing the password.
    Returns:
        True if the password is strong, False otherwise.
    """
    passwordRegex = re.compile(
        r"""
            ^                    # Start of the string anchor
            (?=.*[a-z])          # Ensure string has at least one lowercase letter
            (?=.*[A-Z])          # Ensure string has at least one uppercase letter
            (?=.*\d)             # Ensure string has at least one digit
            (?=.*[!@#$%^&*])     # Ensure string has at least one special character
            .{8,}                # Ensure string has at least 8 characters
            $                    # End of the string anchor
        """,
        re.VERBOSE,
    )

    return True if passwordRegex.findall(password) else False


# Test Cases:
print(is_strong_password("strongPassword"))  # False
print(is_strong_password("StrongPassword"))  # False
print(is_strong_password("StrongPassword1"))  # False
print(is_strong_password("StrongPassword1!"))  # True
print(is_strong_password("StrongPassword1!@"))  # True
print(is_strong_password("StrongPassword1!@#"))  # True
