# @#$^$^*&*(^&$%^#@#@%$#%$^%&*^*&)(&^&%$^@#%$#%^&*&^(&*%$^)#
#                  Sequence Data Types                     #
# @#$^$^*&*(^&$%^#@#@%$#%$^%&*^*&)(&^&%$^@#%$#%^&*&^(&*%$^)#

name = "Zophie"
for i in name:
    print(f"***{i}***")

# @#$^$^*&*(^&$%^#@#@%$#%$^%&*^*&)(&^&%$^@#%$#%^&*&^(&*%$^)#
#            1- Mutable and Immutable Data Types           #
#                 2- The Tauple Data Type                  #
#   3- Converting Types with list() and tuple() functions  #
# @#$^$^*&*(^&$%^#@#@%$#%$^%&*^*&)(&^&%$^@#%$#%^&*&^(&*%$^)#

# 1- Mutable and Immutable Data Types
name = "Zophie a cat."
name[7] = "r"  # TypeError: 'str' object does not support item assignment

# 2- The Tauple Data Type
eggs = ("hello", 42, 0.5)
print(f"The first item in the tuple: {eggs[0]}")
eggs[1] = 99  # TypeError: 'tuple' object does not support item assignment

# 3- Converting Types with list() and tuple() functions
print(f"Converting ['cat', 'dog', 5] list into tuple: {tuple(['cat', 'dog', 5])}")

print(f"Converting ('cat', 'dog', 5) tuple into list: {list(('cat', 'dog', 5))}")

print(f"Converting 'hello!' string into list: {list('hello!')}")
