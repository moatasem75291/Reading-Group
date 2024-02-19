# @#$^$^*&*(^&$%^#@#@%$#%$^%&*^*&)(&^&%$^@#%$#%^&*&^(&*%$^)#
#                   The findall() Method                   #
# @#$^$^*&*(^&$%^#@#@%$#%$^%&*^*&)(&^&%$^@#%$#%^&*&^(&*%$^)#

import re

phoneNumRegex = re.compile(r"\d{3}-\d{3}-\d{4}")
mo = phoneNumRegex.search("Cell: 415-555-9999 Work: 212-555-0000")
print(mo.group())  # output: 415-555-9999

phoneNumRegex = re.compile(r"\d{3}-\d{3}-\d{4}")  # has no groups
mo = phoneNumRegex.findall("Cell: 415-555-9999 Work: 212-555-0000")
print(mo)  # output: ['415-555-9999', '212-555-0000']

phoneNumRegex = re.compile(r"(\d{3})-(\d{3})-(\d{4})")  # has groups
mo = phoneNumRegex.findall("Cell: 415-555-9999 Work: 212-555-0000")
print(mo)  # output: [('415', '555', '9999'), ('212', '555', '0000')]
