# @#$^$^*&*(^&$%^#@#@%$#%$^%&*^*&)(&^&%$^@#%$#%^&*&^(&*%$^)#
#     copying and Pasting String with pyperclip Module     #
# @#$^$^*&*(^&$%^#@#@%$#%$^%&*^*&)(&^&%$^@#%$#%^&*&^(&*%$^)#

"""
The pyperclip module has copy() and paste() functions,
that can send text to and receive text from your computer’s clipboard.

The pyperclip module is not part of the Python Standard Library,
so you have to install it separately.

To install pyperclip, run the following command in your terminal:
'pip install pyperclip'

In this example, we use the copy() function to send 'Hello, world!' to the clipboard,
and then use the paste() function to receive the text from the clipboard.

"""

import pyperclip

pyperclip.copy("Hello, world!")
print(pyperclip.paste())
# Output: Hello, world!
