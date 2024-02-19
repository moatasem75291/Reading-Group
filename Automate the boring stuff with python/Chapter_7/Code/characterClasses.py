# @#$^$^*&*(^&$%^#@#@%$#%$^%&*^*&)(&^&%$^@#%$#%^&*&^(&*%$^)#
#                    Character Classes                     #
# @#$^$^*&*(^&$%^#@#@%$#%$^%&*^*&)(&^&%$^@#%$#%^&*&^(&*%$^)#

""" 
    Character classes are a way to match only one of a specific set of characters.
    A character class is created by putting the characters it matches inside square brackets.
        - For example, the regular expression [aeiou] matches any lowercase vowel.
        - Similarly, [0-9] matches any digit.

    You can also include ranges of letters or numbers by using a hyphen.
        For example, the regular expression [a-zA-Z0-9] matches any lowercase or uppercase letter
            or any digit.

    shorthand character class
        \d - Any numeric digit from 0 to 9.
        \D - Any character that is not a numeric digit from 0 to 9.
        \w - Any letter, numeric digit, or the underscore character. (Think of this as matching “word” characters.)
        \W - Any character that is not a letter, numeric digit, or the underscore character.
        \s - Any space, tab, or newline character. (Think of this as matching “space” characters.)
        \S - Any character that is not a space, tab, or newline.
    
"""

import re

xmasRegex = re.compile(r"\d+\s\w+")
text = (
    "12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, "
    "4 birds, 3 hens, 2 doves, 1 partridge"
)
mo = xmasRegex.findall(text)
print(mo)
