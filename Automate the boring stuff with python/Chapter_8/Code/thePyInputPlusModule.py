# @#$^$^*&*(^&$%^#@#@%$#%$^%&*^*&)(&^&%$^@#%$#%^&*&^(&*%$^)#
#                  The PyInputPlus Module                  #
# 1- The min, max, greaterThan, lessThan Keyword Arguments #
#              2- The blank Keyword Argument               #
#   3- The limit, timeout, and default Keyword Arguments   #
#  4- The allowRegexes and blockRegexes Keyword Arguments  #
#  5- Passing a Custom Validation Functionto inputCustom() #
# @#$^$^*&*(^&$%^#@#@%$#%$^%&*^*&)(&^&%$^@#%$#%^&*&^(&*%$^)#

"""
Writing input validation code for every input() call in your program quicklybecomes tedious.
Also, you miss certain cases and allow invalid input to pass through your checks.
The PyInputPlus module is here to solve these problems.


This module contains functions similar to input() for several kinds of data:
integers, floats, dates, yes/no, and more.
"""
while True:
    print("Enter your age:")
    age = input()
    try:
        age = int(age)
    except:
        print("Please use numeric digits.")
        continue

    if age < 1:
        print("Please enter a valid age.")
        continue
    break
# _________________#_________________#_________________#
import pyinputplus as pyip

response = pyip.inputNum()
print(response)


# 1- The min, max, greaterThan, lessThan Keyword Arguments #
response = pyip.inputNum(
    "Enter Num between [4, 10]: ", min=4, max=10
)  # min, and max are included
print(response)

response = pyip.inputNum("", min=4, lessThan=10)
print(response)

response = pyip.inputNum(
    "", greaterThan=4, lessThan=10
)  # greaterThan, and lessThan are not included
print(response)


#              2- The blank Keyword Argument               #
response = pyip.inputNum("Enter Num: ", blank=True)
print(response)  # blank=True allows the user to skip the input


#   3- The limit, timeout, and default Keyword Arguments   #
response = pyip.inputNum(limit=2)  # limit=2 allows 2 tries
print(response)

response = pyip.inputNum(timeout=10)  # timeout=10 allows 10 seconds
print(response)

response = pyip.inputNum(
    "Enter Num: ", limit=2, default="None"
)  # If no input is given, default="None" will be returned
print(response)


#  4- The allowRegexes and blockRegexes Keyword Arguments  #
response = pyip.inputNum(allowRegexes=[r"(I|V|X|L|C|D|M)+", r"zero"])
print(response)

response = pyip.inputNum(blockRegexes=[r"[02468]$"])
print(response)  # The input must not end with an even number

response = pyip.inputStr(allowRegexes=[r"cat", "dog"], blockRegexes=[r"moose"])
print(response)


# 5- Passing a Custom Validation Functionto inputCustom() #
def addsUpToTen(numbers):
    numbersList = list(numbers)
    for i, digit in enumerate(numbersList):
        numbersList[i] = int(digit)
    if sum(numbersList) != 10:
        raise Exception(f"The digits must add up to 10, not {sum(numbersList)}")
    return int(numbers)


response = pyip.inputCustom(addsUpToTen)
print(response)
