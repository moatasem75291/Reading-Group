# @#$^$^*&*(^&$%^#@#@%$#%$^%&*^*&)(&^&%$^@#%$#%^&*&^(&*%$^)#
#                Case-Insensitive Matching                 #
# @#$^$^*&*(^&$%^#@#@%$#%$^%&*^*&)(&^&%$^@#%$#%^&*&^(&*%$^)#

"""
The re.IGNORECASE / re.I argument can be passed to re.compile() to make the matching case-insensitive.
"""

import re


# The four regexes match completely different strings.
regex1 = re.compile(r"RoboCop")
regex2 = re.compile(r"ROBOCOP")
regex3 = re.compile(r"robOcop")
regex4 = re.compile(r"RobocOp")

print(
    regex1.search("RoboCop ia part man, part machine, all cop.")
)  # <re.Match object; span=(0, 7), match='RoboCop'>
print(regex2.search("RoboCop ia part man, part machine, all cop."))  # None
print(regex3.search("RoboCop ia part man, part machine, all cop."))  # None
print(regex4.search("RoboCop ia part man, part machine, all cop."))  # None


# This regex will be Case-Insensitive.
regex = re.compile(r"robocop", re.IGNORECASE)

print(
    regex.search("RoboCop ia part man, part machine, all cop.").group()
)  # Output: RoboCop
print(
    regex.search("ROBoCop ia part man, part machine, all cop.").group()
)  # Output: ROBoCop
print(
    regex.search("robocop ia part man, part machine, all cop.").group()
)  # Output: robocop
print(
    regex.search("RoBocOP ia part man, part machine, all cop.").group()
)  # Output: RoBocOP
