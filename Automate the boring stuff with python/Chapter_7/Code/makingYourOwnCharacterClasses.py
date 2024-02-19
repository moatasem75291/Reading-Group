# @#$^$^*&*(^&$%^#@#@%$#%$^%&*^*&)(&^&%$^@#%$#%^&*&^(&*%$^)#
#             Making Your Own Character Classes            #
# @#$^$^*&*(^&$%^#@#@%$#%$^%&*^*&)(&^&%$^@#%$#%^&*&^(&*%$^)#

"""
You can also include ranges of letters or numbers by using a hyphen.
For example, the character class [a-zA-Z0-9] will match all lowercase letters,
uppercase letters, and numbers.

By placing a caret character (^) just after the character class’s opening bracket,
you can make a negative character class.

A negative character class will match allthe characters that are not in the character class.
"""

import re

vowelRegex = re.compile(r"[aeiouAEIOU]")
mo = vowelRegex.findall("RoboCop eats baby food. BABY FOOD.")
print(mo)  # output: ['o', 'o', 'o', 'e', 'a', 'a', 'o', 'o', 'A', 'O', 'O']

consonantRegex = re.compile(r"[^aeiouAEIOU]")
mo = consonantRegex.findall("RoboCop eats baby food. BABY FOOD.")
print(mo)
