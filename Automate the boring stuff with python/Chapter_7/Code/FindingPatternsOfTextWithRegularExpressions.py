# @#$^$^*&*(^&$%^#@#@%$#%$^%&*^*&)(&^&%$^@#%$#%^&*&^(&*%$^)#
#    Finding Patterns of Text With Regular Expressions     #
# @#$^$^*&*(^&$%^#@#@%$#%$^%&*^*&)(&^&%$^@#%$#%^&*&^(&*%$^)#

import re


def getPhoneNumber(text: str) -> str:
    """
    This function checks if the given text is a phone number
    Args:
        text (str): The input string to be checked.
    Returns:
        str: The phone number if found, None otherwise.
    """
    phoneNumber = re.compile(r"\d{3}-\d{3}-\d{4}")
    match = phoneNumber.search(text)
    if match:
        return match.group()
    else:
        return None


# Example
message = "Call me at 415-555-1011 tomorrow."
print(f"Phone number found: {getPhoneNumber(message)}")
print("Done")
