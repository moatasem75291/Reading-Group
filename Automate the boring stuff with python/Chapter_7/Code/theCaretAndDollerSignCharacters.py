# @#$^$^*&*(^&$%^#@#@%$#%$^%&*^*&)(&^&%$^@#%$#%^&*&^(&*%$^)#
#           The Caret and Doller Sign Characters           #
# @#$^$^*&*(^&$%^#@#@%$#%$^%&*^*&)(&^&%$^@#%$#%^&*&^(&*%$^)#

"""
The caret and dollar sign characters:

    1- You can also use the caret symbol (^) at the start of a regex to indicate that
        a match must occur at the beginning of the searched text.

    2- Likewise, you can put a dollar sign ($) at the end of the regex to indicate the
        string must end with this regex pattern.

    3- And you can use the ^ and $ together to indicate that the entire string must match
        the regex—that is, it’s not enough for a match to be made on some subset of the string.
"""

import re

beginsWithHello = re.compile(r"^Hello")
mo = beginsWithHello.search("Hello world!")
print(mo.group())  # output: Hello

mo = beginsWithHello.search("He said hello.")
print(mo)  # output: None


endsWithNumber = re.compile(r"\d$")
mo = endsWithNumber.search("Your number is 42")
print(mo.group())  # output: 2

mo = endsWithNumber.search("Your number is forty two.")
print(mo)  # output: None


"""
Carrots cost dollars --> to remind you that the caret comes first and the dollar sign comes last.
🥕 = ^  💰  💵 = $
"""

wholeStringIsNum = re.compile(r"^\d+$")
mo = wholeStringIsNum.search("1234567890")
print(mo.group())  # output: 1234567890

mo = wholeStringIsNum.search("12345xyz67890")
print(mo)  # output: None

mo = wholeStringIsNum.search("12 34567890")
print(mo)  # output: None
