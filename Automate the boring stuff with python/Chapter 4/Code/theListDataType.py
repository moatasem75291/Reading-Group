# @#$^$^*&*(^&$%^#@#@%$#%$^%&*^*&)(&^&%$^@#%$#%^&*&^(&*%$^)#
#                   The List Data Type                     #
# @#$^$^*&*(^&$%^#@#@%$#%$^%&*^*&)(&^&%$^@#%$#%^&*&^(&*%$^)#
numbers = [1, 2, 3]
print(f"List of numbers: {numbers}")

names_of_animals = ["cat", "bat", "rat", "elephent"]
print(f"List of names: {names_of_animals}")

multible_items = ["hello", 3.1415, True, None, 5]
print(f"List of multible items: {multible_items}")

# @#$^$^*&*(^&$%^#@#@%$#%$^%&*^*&)(&^&%$^@#%$#%^&*&^(&*%$^)#
#    1- Getting individualvalues in a list with indexes    #
#                    2- Negative indexes                   #
#      3- Getting a List from another listwith Slices      #
#    4- Getting a List's Length with the len() function    #
#         5- Getting Values in a list with indexes         #
#        6- List Concatenation and List Replication        #
#     7- Removing values from Lists with del Statements    #
# @#$^$^*&*(^&$%^#@#@%$#%$^%&*^*&)(&^&%$^@#%$#%^&*&^(&*%$^)#

# 1- Getting individualvalues in a list with indexes
spam = ["cat", "bat", "rat", "elephent"]
print("The first index: ", spam[0])

spam = ["cat", "bat", "rat", "elephent"]
print("The second index: ", spam[1])

spam = ["cat", "bat", "rat", "elephent"]
print("The third index: ", spam[2])

message = "Hello, " + spam[0] + "!"
print(message)

sentence = f"The {spam[1]} ate the {spam[0]}."
print(sentence)

spam = [
    ["cat", "bat"],
    [10, 20, 30, 40, 50],
]
print(f"The first list in the list: {spam[0]}")
print(f"The second item in the first list: {spam[0][1]}")
print(f"The last item in the second list: {spam[1][4]}")

# 2- Negative indexes
spam = ["cat", "bat", "rat", "elephent"]
print(f"The last item: {spam[-1]}")

sentence = f"The {spam[-1]} is afraid of the {spam[-3]}."
print(sentence)

# 3- Getting a List from another listwith Slices
spam = ["cat", "bat", "rat", "elephent"]
print(f"The list items using slicing: {spam[0:4]}")
print(f"The second and third items using slicing: {spam[1:3]}")
print(f"The list items without the last one: {spam[0:-1]}")
print(f"The first and second items without specifies the first index: {spam[:2]}")
print(f"The list items without the first: {spam[1:]}")
print(f"The list items: {spam[:]}")

# 4- Getting a List's Length with the len() function
spam = ["cat", "dog", "moose"]
print(f"The Length of the spam list is: {len(spam)}.")

# 5- Getting Values in a list with indexes
spam = ["cat", "bat", "rat", "elephent"]
print("The List before reassigning: ", spam)
spam[1] = "aardvark"
spam[-1] = 132434
print("The List after reassigning: ", spam)

# 6- List Concatenation and List Replication
numbers = [1, 2, 3]
characters = ["A", "B", "C"]
print(
    f"Concatenate the numbers with characters using + operator: {numbers + characters}"
)
print(f"Replicate the characters list using * operator: {characters * 3}")

# 7- Removing values from Lists with del Statements
spam = ["cat", "bat", "rat", "elephent"]
print("The List before deletion: ", spam)
del spam[2]
print("The List after deletion: ", spam)
