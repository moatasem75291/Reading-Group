# @#$^$^*&*(^&$%^#@#@%$#%$^%&*^*&)(&^&%$^@#%$#%^&*&^(&*%$^)#
#              Greedy and Non-greedy Matching              #
# @#$^$^*&*(^&$%^#@#@%$#%$^%&*^*&)(&^&%$^@#%$#%^&*&^(&*%$^)#

import re

greedyHaRegex = re.compile(r"(Ha){3,5}")
mo1 = greedyHaRegex.search("HaHaHaHaHaHa")
print(f"Greedy Match: {mo1.group()}")  # HaHaHaHaHa

nongreedyHaRegex = re.compile(r"(Ha){3,5}?")
mo2 = nongreedyHaRegex.search("HaHaHaHaHa")
print(f"Non-greedy Match: {mo2.group()}")
