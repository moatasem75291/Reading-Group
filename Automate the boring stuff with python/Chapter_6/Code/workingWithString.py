# @#$^$^*&*(^&$%^#@#@%$#%$^%&*^*&)(&^&%$^@#%$#%^&*&^(&*%$^)#
#                   Working With String                    #
#                    1- String Literals                    #
#             2- Indexing and Slicing String               #
#       3- The in and not in Operators with Strings        #
# @#$^$^*&*(^&$%^#@#@%$#%$^%&*^*&)(&^&%$^@#%$#%^&*&^(&*%$^)#

#                    1- String Literals                    #
spam = "This is Alice's cat."  # Double quote

spam = "Say hi to Bob's mother"  # Escape Character
spam = "Hello there!\n How are you?\n I'm doing fine."

print(r"That is Carol\'s cat.")  # raw string
print(
    """Dear Alice,
Eve's cat has been arrested for catnapping, cat burglary, and extortion.
Sincerely,
Bob"""
)  # Multiline Strings with Triple Quotes

"""This a test Python program.
Written by Al Sweigart al@inventwithpython.com
This program was designed for Python 3, not Python 2.
"""  # Multiline Comments


def spam():
    """This is a multiline comment to help
    explain what the spam() function does."""
    print("Hello!")


#             2- Indexing and Slicing String               #
spam = "Hello World!"
print(spam[0])
print(spam[4])
print(spam[-1])
print(spam[0:5])
print(spam[:5])
print(spam[6:])

fizz = spam[0:5]
print(fizz)


#       3- The in and not in Operators with Strings        #
print("Hello" in "Hello World")
print("Hello" in "Hello")
print("HELLO" in "Hello World")
print("" in "Hello World")
print("cats" not in "cats and dogs")
