# @#$^$^*&*(^&$%^#@#@%$#%$^%&*^*&)(&^&%$^@#%$#%^&*&^(&*%$^)#
#                       Refrences                          #
# @#$^$^*&*(^&$%^#@#@%$#%$^%&*^*&)(&^&%$^@#%$#%^&*&^(&*%$^)#

# in Variables
spam = 42
cheese = spam
spam = 100
print(spam)  # spam: 100
print(cheese)  # cheese: 42

# in Lists
spam = [0, 1, 2, 3, 4, 5]
cheese = spam
cheese[1] = "hello!"
print(spam)  # spam: [0, 1, 2, 3, 4, 5]
print(cheese)  # cheese: [0, 1, 2, 3, 4, 5]

# @#$^$^*&*(^&$%^#@#@%$#%$^%&*^*&)(&^&%$^@#%$#%^&*&^(&*%$^)#
#             1- Identify and the id() Function            #
#                   2- Passing Refrences                   #
#   3- The copy Module's cope() and deepcopy() functions   #
# @#$^$^*&*(^&$%^#@#@%$#%$^%&*^*&)(&^&%$^@#%$#%^&*&^(&*%$^)#

# 1- Identify and the id() Function
print(id("Mo3tsm"))

bacon = "Hello,"
id(bacon)
bacon += " world!"
id(bacon)  # The id changed, bacon now refers to a completely different string.

eggs = ["cat", "dog"]
id(eggs)
eggs.append("moose")
id(eggs)  # refers to the same list as bfeor.


# 2- Passing Refrences
def eggs(someParameter):
    someParameter.append("hello")


spam = [1, 2, 3, 4]
eggs(spam)
print(spam)

# 3- The copy Module's cope() and deepcopy() functions
import copy

spam = ["A", "B", "C", "D"]
id(spam)

cheese = copy.copy(spam)
id(cheese)  # cheese is different list with different identity.

spam = [
    ["A", "B"],
    ["C", "D"],
]
id(spam)

cheese = copy.deepcopy(spam)
id(cheese)
