# @#$^$^*&*(^&$%^#@#@%$#%$^%&*^*&)(&^&%$^@#%$#%^&*&^(&*%$^)#
#                 Managing Complex Regexes                 #
# @#$^$^*&*(^&$%^#@#@%$#%$^%&*^*&)(&^&%$^@#%$#%^&*&^(&*%$^)#

"""
You can mitigate this by telling the re.compile() function to ignore whitespace and comments
    inside the regular expression string.
This “verbose mode” can be enabled by passing the variable re.VERBOSE as the second argument to re.compile().

"""

import re


# Now instead of a hard-to-read regular expression like this:
phoneRegex = re.compile(
    r"((\d{3}|\(\d{3}\))?(\s|-|\.)?\d{3}(\s|-|\.)\d{4}(\s*(ext|x|ext.)\s*\d{2,5})?)"
)

# You can spread the regular expression over multiple lines with comments like this:
phoneRegex = re.compile(
    r"""(
    (\d{3}|\(\d{3}\))?            # area code
    (\s|-|\.)?                    # separator
    \d{3}                         # first 3 digits
    (\s|-|\.)                     # separator
    \d{4}                         # last 4 digits
    (\s*(ext|x|ext.)\s*\d{2,5})?  # extension
    )""",
    re.VERBOSE,
)

phone = "Call me at 415-555-1011 tomorrow. (415) 555-9999 is my office."
mo = phoneRegex.findall(phone)
print(mo)
# Output: [('415-555-1011', '415', '-', '-', '', ''), ('(415) 555-9999', '(415)', ' ', '-', '', '')]

# ________________________________________________________________________________ #

# @#$^$^*&*(^&$%^#@#@%$#%$^%&*^*&)(&^&%$^@#%$#%^&*&^(&*%$^)#
#    Combining re.IGNORECASE, re.DOTALL, and re.VERBOSE    #
# @#$^$^*&*(^&$%^#@#@%$#%$^%&*^*&)(&^&%$^@#%$#%^&*&^(&*%$^)#

"""
You can even combine re.IGNORECASE, re.DOTALL, and re.VERBOSE using the pipe character (|),
    which in this context is known as the bitwise or operator.

"""

someRegexValue = re.compile("foo", re.IGNORECASE | re.DOTALL | re.VERBOSE)
mo = someRegexValue.match("foo")
print(mo)
# Output: <re.Match object; span=(0, 3), match='foo'>
