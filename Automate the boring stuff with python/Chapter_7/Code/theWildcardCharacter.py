# @#$^$^*&*(^&$%^#@#@%$#%$^%&*^*&)(&^&%$^@#%$#%^&*&^(&*%$^)#
#                  The Wildcard Character                  #
#           1- Matching Everyything with Dot-Star          #
#        2- Matching Newlines with the Dot Character       #
# @#$^$^*&*(^&$%^#@#@%$#%$^%&*^*&)(&^&%$^@#%$#%^&*&^(&*%$^)#

import re

atRegex = re.compile(r".at")
print(atRegex.findall("The cat in the hat sat on the flat mat."))


#           1- Matching Everyything with Dot-Star          #

nameRegex = re.compile(r"First Name: (.*) Last Name: (.*)")  # .* is greedy
mo = nameRegex.search("First Name: Al Last Name: Sweigart")
print(mo.group(1))
print(mo.group(2))

nongreedyRegex = re.compile(r"<.*?>")  # .*? is non-greedy
mo = nongreedyRegex.search("<To serve man> for dinner.>")
print(mo.group())

greedyRegex = re.compile(r"<.*>")  # .* is greedy
mo = greedyRegex.search("<To serve man> for dinner.>")
print(mo.group())


#        2- Matching Newlines with the Dot Character       #

noNewlineRegex = re.compile(".*")
print(
    noNewlineRegex.search(
        "Serve the public trust.\nProtect the innocent.\nUphold the law."
    ).group()
)

newlineRegex = re.compile(".*", re.DOTALL)
print(
    newlineRegex.search(
        "Serve the public trust.\nProtect the innocent.\nUphold the law."
    ).group()
)
