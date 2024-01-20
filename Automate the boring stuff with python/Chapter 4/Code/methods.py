# @#$^$^*&*(^&$%^#@#@%$#%$^%&*^*&)(&^&%$^@#%$#%^&*&^(&*%$^)#
#      1- Finding a vlue in a List with index() Method     #
# 2- Adding Values to List with append(), insert() Methods #
#    3- Removing Values from List with remove() Method     #
#    4- Sorting Values in a List with the sort() Method    #
#  5- Reversing Values in a list with the reverse() Method #
# @#$^$^*&*(^&$%^#@#@%$#%$^%&*^*&)(&^&%$^@#%$#%^&*&^(&*%$^)#

# 1- Finding a vlue in a List with index() Method
spam = ["hello", "hi", "howdy", "heyas"]
print(f"The index of howdy item is: {spam.index('howdy')}")

spam = ["Zophie", "Pooka", "Fat-tail", "Pooka"]
print(f"The index of repeated Pooka item is: {spam.index('Pooka')}")

# 2- Adding Values to List with append(), insert() Methods
spam = ["cat", "dog", "bat"]
spam.append("checken")
print(f"The list after adding the item `checken` using append method: {spam}")

spam.insert(2, "moose")
print(f"The list after adding the item `moose` using insert method: {spam}")

# 3- Removing Values from List with remove() Method
spam = ["cat", "bat", "rat", "elephent"]
spam.remove("rat")
print(f"The list after removing the item `rat` using remove method: {spam}")

# 4- Sorting Values in a List with the sort() Method
spam = [2, 5, 3.1415, -7, 1]
spam.sort()
print(f"The list after sorting the items using sort method: {spam}")

# 5- Reversing Values in a list with the reverse() Method
spam = ["cat", "dog", "bat"]
spam.reverse()
print(f"The list after reverseing the items using reverse method: {spam}")
