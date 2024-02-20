# @#$^$^*&*(^&$%^#@#@%$#%$^%&*^*&)(&^&%$^@#%$#%^&*&^(&*%$^)#
#        Substituting Strings with the sub() Method        #
# @#$^$^*&*(^&$%^#@#@%$#%$^%&*^*&)(&^&%$^@#%$#%^&*&^(&*%$^)#

"""
The sub() method for Regex objects is passed two arguments.
    - The first argument is a string to replace any matches.
    - The second argument is the string for the regular expression.
The sub() method returns a string with the substitutions applied.

"""

import re

namesRegex = re.compile(r"Agent \w+")
print(namesRegex.sub("CENSORED", "Agent Alice gave the secret documents to Agent Bob."))
# Output: CENSORED gave the secret documents to CENSORED.


# Example
agentNamesRegex = re.compile(r"Agent (\w)\w*")
print(
    agentNamesRegex.sub(
        r"\1****",
        "Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.",
    )
)
# Output: A**** told C**** that E**** knew B**** was a double agent.
