# @#$^$^*&*(^&$%^#@#@%$#%$^%&*^*&)(&^&%$^@#%$#%^&*&^(&*%$^)#
#  Numeric Values Of Characters with the ord(), and chr()  #
# @#$^$^*&*(^&$%^#@#@%$#%$^%&*^*&)(&^&%$^@#%$#%^&*&^(&*%$^)#

# The ord() function returns the numeric value of a simple ASCII character
print(ord("A"))  # Output: 65
print(ord("B"))  # Output: 66
print(ord("C"))  # Output: 67
print(ord("a"))  # Output: 97
print(ord("b"))  # Output: 98
print(ord("c"))  # Output: 99
print(ord("0"))  # Output: 48
print(ord("1"))  # Output: 49
print(ord("2"))  # Output: 50
print(ord("!"))  # Output: 33
print(ord("@"))  # Output: 64
print(ord("#"))  # Output: 35

# The chr() function returns the character of a simple ASCII numeric value
print(chr(65))  # Output: A
print(chr(66))  # Output: B
print(chr(67))  # Output: C
print(chr(97))  # Output: a
print(chr(98))  # Output: b
print(chr(99))  # Output: c
print(chr(48))  # Output: 0
print(chr(49))  # Output: 1
print(chr(50))  # Output: 2
print(chr(33))  # Output: !
print(chr(64))  # Output: @
print(chr(35))  # Output: #

# The ord() and chr() functions are inverses of each other
print(chr(ord("A")))  # Output: A
print(chr(ord("B")))  # Output: B
print(chr(ord("C") + 1))  # Output: D
