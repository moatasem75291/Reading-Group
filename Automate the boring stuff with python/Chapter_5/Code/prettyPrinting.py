# @#$^$^*&*(^&$%^#@#@%$#%$^%&*^*&)(&^&%$^@#%$#%^&*&^(&*%$^)#
#                      Pretty Printing                     #
# @#$^$^*&*(^&$%^#@#@%$#%$^%&*^*&)(&^&%$^@#%$#%^&*&^(&*%$^)#

import pprint

message = "It was a bright cold day in April, and the clocks were striking thirteen."
count = {}
for i in message:
    count.setdefault(i, 0)
    count[i] += 1
pprint.pprint(count, indent=10, depth=30, sort_dicts=False)

# pprint/pformat with nestead dictionaries
message = "It was a bright cold day in April, and the clocks were striking thirteen."
count = {}
for i in message:
    count.setdefault(i, {})
    count[i].setdefault("count", 0)
    count[i]["count"] += 1

pprint.pprint(count, indent=10, sort_dicts=False)
print(pprint.pformat(count, indent=10, sort_dicts=False))
