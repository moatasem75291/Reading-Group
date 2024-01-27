"""
The first part:

You are creating a fntasy video game. The data structure to model
the player's inventory will be a dictionary where the keys are string
values describing the item in the inventory and the value is an integer
value detailing how many of that item the player has. For example, the
dictionary value {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1,
'arrow': 12} means the player has 1 rope, 6 torches, 42 gold coins, and
so on.

Write a function named displayInventory() that would take any possible
"inventory" and display it like the following:
Inventory:
12 arrow
42 gold coin
1 rope
6 torch
1 dagger
Total number of items: 62

The function should handle cases when there are no items in the inventory
and when there is only one item. Also, an added bonus would be to sort
the items in the inventory alphabetically.
________________________________________________________________________

The second part:

Imagine that a vanquished dragon's loot is represented as a list of strings
like this:
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
Write a function named addToInventory(inventory, addedItems), where the
inventory parameter is a dictionary representing the player's inventory
(like in the previous project) and the addedItems parameter is a list like
dragonLoot. The addToInventory() function should return a dictionary that
represents the updated inventory. Note that the addedItems list can contain
multiples of the same item.

"""
# @#$^$^*&*(^&$%^#@#@%$#%$^%&*^*&)(&^&%$^@#%$#%^&*&^(&*%$^)#
#                 1- Fntasy Game Inventory                 #
# 2- List to Dictionary Function for Fntasy Game Inventory #
# @#$^$^*&*(^&$%^#@#@%$#%$^%&*^*&)(&^&%$^@#%$#%^&*&^(&*%$^)#


#                 1- Fntasy Game Inventory                 #
def displayInventory(inv):
    print("Inventory:")
    item_total = 0
    for k, v in sorted(inv.items()):
        print(str(v) + " " + k)
        item_total += v
    print("Total number of items: " + str(item_total))


# Test Cases
# inv = {'gold coin': 42, 'rope': 1}
inv = {"gold coin": 42, "rope": 1}
displayInventory(inv)
# inv = {'gold coin': 42, 'rope': 1, 'torch': 6, 'dagger': 1, 'arrow': 12}
inv = {"gold coin": 42, "rope": 1, "torch": 6, "dagger": 1, "arrow": 12}
displayInventory(inv)
# inv = {}
inv = {}
displayInventory(inv)


# 2- List to Dictionary Function for Fntasy Game Inventory #
def addToInventory(inventory: dict, addedItems):
    for item in addedItems:
        inventory.setdefault(item, 0)
        inventory[item] += 1
    return inventory


# Test Case
inv = {"gold coin": 42, "rope": 1}
dragonLoot = ["gold coin", "dagger", "gold coin", "gold coin", "ruby"]
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)
