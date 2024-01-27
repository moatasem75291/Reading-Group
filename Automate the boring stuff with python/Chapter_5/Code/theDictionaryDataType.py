# @#$^$^*&*(^&$%^#@#@%$#%$^%&*^*&)(&^&%$^@#%$#%^&*&^(&*%$^)#
#                 The Dictionary Data Type                 #
# @#$^$^*&*(^&$%^#@#@%$#%$^%&*^*&)(&^&%$^@#%$#%^&*&^(&*%$^)#

myCat = {"size": "fat", "color": "gray", "disposition": "loud"}
print(myCat["size"])
print("My cat has " + myCat["color"] + " fur.")

# @#$^$^*&*(^&$%^#@#@%$#%$^%&*^*&)(&^&%$^@#%$#%^&*&^(&*%$^)#
#                 1- Dictionaries vs. Lists                #
#       2- The keys(), values(). and items() Methods       #
# 3- Checking whether a Key or Value Exist in a Dictionary #
#                    4- The get() Method                   #
#                 5- The setdefault() Method               #
# @#$^$^*&*(^&$%^#@#@%$#%$^%&*^*&)(&^&%$^@#%$#%^&*&^(&*%$^)#

# 1- Dictionaries vs. Lists
spam = ["cats", "dogs", "moose"]
bacon = ["dogs", "moose", "cats"]
print(spam == bacon)  # False
eggs = {"name": "Zophie", "species": "cat", "age": "8"}
ham = {"species": "cat", "age": "8", "name": "Zophie"}
print(eggs == ham)  # True

# birthdays.py
birthdays = {"Alice": "Apr 1", "Bob": "Dec 12", "Carol": "Mar 4"}
while True:
    print("Enter a name: (blank to quit)")
    name = input()
    if name == "":
        break
    if name in birthdays:
        print(birthdays[name] + " is the birthday of " + name)
    else:
        print("I do not have birthday information for " + name)
        print("What is their birthday?")
        bday = input()
        birthdays[name] = bday
        print("Birthday database updated.")

# Ordered Dictionaries in Python
eggs = {"name": "Zophie", "species": "cat", "age": "8"}
print(list(eggs))  # ['name', 'species', 'age']
ham = {"species": "cat", "age": "8", "name": "Zophie"}
print(list(ham))  # ['species', 'age', 'name']

# 2- The keys(), values(). and items() Methods
spam = {"color": "red", "age": 42}
for v in spam.values():
    print(v)

for k in spam.keys():
    print(k)

for i in spam.items():
    print(i)

# Multiple assignment trick
spam = {"color": "red", "age": 42}
for k, v in spam.items():
    print("Key: " + k + " Value: " + str(v))

# 3- Checking Whether a Key or Value Exist in a Dictionary
spam = {"name": "Zophie", "age": 7}
print("name" in spam.keys())  # True
print("Zophie" in spam.values())  # True
print("color" in spam.keys())  # False
print("color" not in spam.keys())  # True
print("color" in spam)  # False

# 4- The get() Method
picnicItems = {"apples": 5, "cups": 2}
print("I am bringing " + str(picnicItems.get("cups", 0)) + " cups.")
print("I am bringing " + str(picnicItems.get("eggs", 0)) + " eggs.")

# 5- The setdefault() Method
spam = {"name": "Pooka", "age": 5}
if "color" not in spam:
    spam["color"] = "black"
print(spam)  # {'name': 'Pooka', 'age': 5, 'color': 'black'}

spam = {"name": "Pooka", "age": 5}
spam.setdefault("color", "black")  # 'black'
print(spam)  # {'name': 'Pooka', 'age': 5, 'color': 'black'}
spam.setdefault("color", "white")  # 'black'(-_-)!?
print(spam)  # {'name': 'Pooka', 'age': 5, 'color': 'black'}

# characterCount.py
message = "It was a bright cold day in April, and the clocks were striking thirteen."
count = {}
for i in message:
    count.setdefault(i, 0)
    count[i] += 1

print(count)
