# @#$^$^*&*(^&$%^#@#@%$#%$^%&*^*&)(&^&%$^@#%$#%^&*&^(&*%$^)#
#                  Useful String Methods                   #
#   1- The upper(), lower(), isupper(), islower() Methods  #
#                  2- The isX() Methods                    #
#        4- The startswith() and endswith() Methods        #
#             5- The join() and split() Methods            #
#     6- Splitting Strings with the partition() Method     #
#      7- The rjust(), ljust(), and center() Methods       #
#      8- The strip(), rstrip(), and lstrip() Methods      #
# @#$^$^*&*(^&$%^#@#@%$#%$^%&*^*&)(&^&%$^@#%$#%^&*&^(&*%$^)#

#   1- The upper(), lower(), isupper(), islower() Methods  #
spam = "Hello World!"
print(spam.upper())
print(spam.lower())

print("How are you?")
answer = input()
if answer.lower() == "fine":
    print("That is good to hear.")
else:
    print("I hope the rest of your day is good.")

spam = "Hello World!"
print(spam.islower())  # False
print(spam.isupper())  # False
print("HELLO".isupper())  # True
print("abc12345".islower())  # True
print("12345".islower())  # False
print("12345".isupper())  # False

"Hello".upper()  # 'HELLO'
"Hello".upper().lower()  # 'hello'
"Hello".upper().lower().upper()  # 'HELLO'
"HELLO".lower()  # 'hello'
"HELLO".lower().islower()  # True

#                  2- The isX() Methods                    #
print("hello".isalpha())  # True, because it contains no non-alphabetical characters
print("hello123".isalpha())  # False, because it contains non-alphabetical characters
print(
    "hello123".isalnum()
)  # True, because it contains only alphabetical and numeric characters
print(
    "hello".isalnum()
)  # True, because it contains only alphabetical and numeric characters
print("123".isdecimal())  # True, because it contains only numeric characters
print(" ".isspace())  # True, because it contains only space characters
print(
    "This Is Title Case".istitle()
)  # True, because it contains only words that begin with an uppercase letter followed by only lowercase letters
print(
    "This Is Title Case 123".istitle()
)  # True, because it contains only words that begin with an uppercase letter followed by only lowercase letters
print(
    "This Is not Title Case".istitle()
)  # False, because it contains a word that is not title case (i.e., does not start with a capital letter).
print(
    "This Is NOT Title Case Either".istitle()
)  # False, because it contains a word that is not title case (i.e., does not start with a capital letter).


# validateInput.py
while True:
    print("Enter your age:")
    age = input()
    if age.isdecimal():
        break
    print("Please enter a number for your age.")

while True:
    print("Select a new password (letters and numbers only):")
    password = input()
    if password.isalnum():
        break
    print("Passwords can only have letters and numbers.")


#        4- The startswith() and endswith() Methods        #
print("Hello World!".startswith("Hello"))  # True
print("Hello World!".endswith("World!"))  # True
print("abc123".startswith("abcdef"))  # False
print("abc123".endswith("12"))  # False
print("Hello World!".startswith("Hello World!"))  # True
print("Hello World!".endswith("Hello World!"))  # True


#             5- The join() and split() Methods            #
print(", ".join(["cats", "rats", "bats"]))  # 'cats, rats, bats'
print(" ".join(["My", "name", "is", "Simon"]))  # 'My name is Simon'
print("ABC".join(["My", "name", "is", "Simon"]))  # 'MyABCnameABCisABCSimon'
print("My name is Simon".split())  # ['My', 'name', 'is', 'Simon']
print("MyABCnameABCisABCSimon".split("ABC"))  # ['My', 'name', 'is', 'Simon']
print("My name is Simon".split("m"))  # ['My na', 'e is Si', 'on']

spam = """Dear Alice,
How have you been? I am fine.
There is a container in the fridge
that is labeled "Milk Experiment".

Please do not drink it.
Sincerely,
Bob"""
print(spam.split("\n"))


#     6- Splitting Strings with the partition() Method     #
print("Hello, world!".partition("w"))  # ('Hello, ', 'w', 'orld!')
print("Hello, world!".partition("world"))  # ('Hello, ', 'world', '!')
print("Hello, world!".partition("o"))  # ('Hell', 'o', ', world!')
print("Hello, world!".partition("x"))  # ('Hello, world!', '', '')
before, sep, after = "Hello, world!".partition(" ")
print(before)  # Hello,
print(sep)  # ' '
print(after)  # world!


#      7- The rjust(), ljust(), and center() Methods       #
print("Hello".rjust(10))  # '     Hello'
print("Hello".ljust(10))  # 'Hello     '
print("Hello".rjust(20, "*"))  # '***************Hello'
print("Hello".ljust(20, "-"))  # 'Hello---------------'
print("Hello".center(20))  # '       Hello        '
print("Hello".center(20, "="))  # '=======Hello========'


# pinicTable.py
def printPicnic(itemsDict, leftWidth, rightWidth):
    print("PICNIC ITEMS".center(leftWidth + rightWidth + 1, "-"))
    for k, v in itemsDict.items():
        print(k.ljust(leftWidth, ".") + " " + str(v).rjust(rightWidth, "."))


picnicItems = {
    "sandwiches": 4,
    "apples": 12,
    "cups": 4,
    "cookies": 8000,
}
printPicnic(picnicItems, 12, 5)
printPicnic(picnicItems, 20, 6)


#      8- The strip(), rstrip(), and lstrip() Methods      #
spam = "    Hello World     "
print(spam.strip())  # Hello World
print(spam.lstrip())  # Hello World
print(spam.rstrip())  #     Hello World

spam = "SpamSpamBaconSpamEggsSpamSpam"
print(spam.strip("ampS"))  # 'BaconSpamEggs'
