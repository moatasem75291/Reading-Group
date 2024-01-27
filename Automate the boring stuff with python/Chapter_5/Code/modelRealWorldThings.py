# @#$^$^*&*(^&$%^#@#@%$#%$^%&*^*&)(&^&%$^@#%$#%^&*&^(&*%$^)#
#     Using Data Structure to Model Real-World Things      #
#                  1- A Tic-Tac-Toe Board                  #
#            2- Nested Dictionaries and Lists              #
# @#$^$^*&*(^&$%^#@#@%$#%$^%&*^*&)(&^&%$^@#%$#%^&*&^(&*%$^)#

#                  1- A Tic-Tac-Toe Board                  #
theBoard = {
    "top-L": " ",
    "top-M": " ",
    "top-R": " ",
    "mid-L": " ",
    "mid-M": " ",
    "mid-R": " ",
    "low-L": " ",
    "low-M": " ",
    "low-R": " ",
}


def print_board(board):
    print(board["top-L"] + "|" + board["top-M"] + "|" + board["top-R"])
    print("-+-+-")
    print(board["mid-L"] + "|" + board["mid-M"] + "|" + board["mid-R"])
    print("-+-+-")
    print(board["low-L"] + "|" + board["low-M"] + "|" + board["low-R"])


print_board(theBoard)

theBoard = {
    "top-L": "O",
    "top-M": "O",
    "top-R": "O",
    "mid-L": "X",
    "mid-M": "X",
    "mid-R": " ",
    "low-L": " ",
    "low-M": " ",
    "low-R": "X",
}
print_board(theBoard)

# add code that allows the players to enter their moves
# ticTacToy.py
theBoard = {
    "top-L": " ",
    "top-M": " ",
    "top-R": " ",
    "mid-L": " ",
    "mid-M": " ",
    "mid-R": " ",
    "low-L": " ",
    "low-M": " ",
    "low-R": " ",
}
turn = "X"
for i in range(9):
    print_board(theBoard)
    print("Turn for " + turn + ". Move on which space?")
    move = input()
    theBoard[move] = turn
    if turn == "X":
        turn = "O"
    else:
        turn = "X"

#            2- Nested Dictionaries and Lists              #
allGuests = {
    "Alice": {"apples": 5, "pretzels": 12},
    "Bob": {"ham sandwiches": 3, "apples": 2},
    "Carol": {"cups": 3, "apple pies": 1},
}
guestList = list(allGuests.keys())
print(guestList)


def totalBrought(guestes, item):
    numBrought = 0
    for _, v in guestes.items():
        numBrought = numBrought + v.get(item, 0)
    return numBrought


print("Number of things being brought:")
print(" - Apples " + str(totalBrought(allGuests, "apples")))
print(" - Cups " + str(totalBrought(allGuests, "cups")))
print(" - Cakes " + str(totalBrought(allGuests, "cakes")))
print(" - Ham Sandwiches " + str(totalBrought(allGuests, "ham sandwiches")))
print(" - Apple Pies " + str(totalBrought(allGuests, "apple pies")))
print(" - Pretzels " + str(totalBrought(allGuests, "pretzels")))
