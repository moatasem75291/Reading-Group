# @#$^$^*&*(^&$%^#@#@%$#%$^%&*^*&)(&^&%$^@#%$#%^&*&^(&*%$^)#
#   Finding Patterns of Text Without Regular Expressions   #
# @#$^$^*&*(^&$%^#@#@%$#%$^%&*^*&)(&^&%$^@#%$#%^&*&^(&*%$^)#


def isPhoneNumber(text: str) -> bool:
    """
    This function checks if the given text is a phone number
    Args:
        text (str): The input string to be checked.
    Returns:
        bool: True if the input string is a phone number, False otherwise.
    """
    if len(text) != 12:  # the length of the phone number is 12
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():  # the three decimal places are not digits
            return False
    if text[3] != "-":  # the fourth character is not a hyphen
        return False
    for i in range(4, 7):  # the next three characters are not digits
        if not text[i].isdecimal():
            return False
    if text[7] != "-":  # the eighth character is not a hyphen
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():  # the last four characters are not digits
            return False
    return True


# Example
message = "Call me at 415-555-1011 tomorrow. 415-555-9999 is my office."
for i in range(len(message)):
    chunk = message[i : i + 12]
    if isPhoneNumber(chunk):
        print(f"Phone number found: {chunk}")

print("Done")
