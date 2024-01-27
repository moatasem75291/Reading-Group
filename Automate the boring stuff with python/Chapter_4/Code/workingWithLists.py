# @#$^$^*&*(^&$%^#@#@%$#%$^%&*^*&)(&^&%$^@#%$#%^&*&^(&*%$^)#
#                   Working with Lists                     #
# @#$^$^*&*(^&$%^#@#@%$#%$^%&*^*&)(&^&%$^@#%$#%^&*&^(&*%$^)#

# allMyCats1, the bad way
print("Enter the name of cat 1: ")
catName1 = input()
print("Enter the name of cat 2: ")
catName2 = input()
print("Enter the name of cat 3: ")
catName3 = input()
print("Enter the name of cat 4: ")
catName4 = input()
print("Enter the name of cat 5: ")
catName5 = input()
print("Enter the name of cat 6: ")
catName6 = input()

print("The cats name are:")
print(
    catName1
    + " "
    + catName2
    + " "
    + catName3
    + " "
    + catName4
    + " "
    + catName5
    + " "
    + catName6
)

# allMyCats2, the improved version
catNames = []
while True:
    print(
        f"Enter the name of cat, {str(len(catNames) + 1)}. (or Enter nothing to stop.):"
    )
    catName = input()
    if catName == "":
        break
    catNames = catNames + [catName]
print("The Cat names are: ")
for name in catNames:
    print("    " + name)

# @#$^$^*&*(^&$%^#@#@%$#%$^%&*^*&)(&^&%$^@#%$#%^&*&^(&*%$^)#
#               1- Using for Loops with Lists              #
#              2- The in and not in Operators              #
#             3- The Multiple Assignment trick             #
#       4- Using the enumerate() function with Lists       #
#  5- from Random Using choice(), and shuffle() with Lists #
# @#$^$^*&*(^&$%^#@#@%$#%$^%&*^*&)(&^&%$^@#%$#%^&*&^(&*%$^)#

# 1- Using for Loops with Lists
supplies = ["pens", "staplers", "flamethrowers", "binders"]
for i in range(len(supplies)):
    print(f"Index {i} in supplies is: {supplies[i]}")

# 2- The in and not in Operators
print(
    "is howdy in this list, ['hello', 'hi', 'howdy', 'heyas']?\n",
    "howdy" in ["hello", "hi", "howdy", "heyas"],
)
print(
    "is cat not in this list, ['hello', 'hi', 'cat', 'heyas']?\n",
    "cat" not in ["hello", "hi", "cat", "heyas"],
)

# myPets
myPets = ["Zophie", "Pooka", "Fat-tail"]
print("Enter a pet name:")
name = input()
if name not in myPets:
    print("I don't have a pet named, ", name)
else:
    print(name, " is my pet")

# 3- The Multiple Assignment trick
cat = ["fat", "grey", "loud"]

size = cat[0]
color = cat[1]
disposition = cat[2]
print(f"without tuple unpacking: size {size}, color {color}, disposition {disposition}")
# with tuple unpacking
size, color, disposition = cat
print(f"with tuple unpacking: size {size}, color {color}, disposition {disposition}")

# 4- Using the enumerate() function with Lists
supplies = ["pens", "staplers", "flamethrowers", "binders"]
for index, item in enumerate(supplies):
    print(f"Index {index} in supplies is: {item}")

# 5- from Random Using choice(), and shuffle() with Lists
import random

pets = ["cat", "dog", "moose"]
print(random.choice(pets))
print(random.choice(pets))

people = ["Alice", "Bob", "Carol", "David"]
random.shuffle(people)
print(people)
random.shuffle(people)
print(people)
