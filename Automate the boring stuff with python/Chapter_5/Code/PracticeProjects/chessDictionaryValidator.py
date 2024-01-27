"""
Write a function named isValidChessBoard() that takes a dictionary
argument and returns True or False depending on if the board is valid.
A valid board will have exactly one black king and exactly one white king.
Each player can only have at most 16 pieces, at most 8 pawns, and all pieces
must be on a valid space from '1a' to '8h'; that is, a piece can’t be on space'9z'.
The piece names begin with either a 'w' or 'b' to represent white or black, followed by
'pawn', 'knight', 'bishop', 'rook', 'queen', or 'king'.
This function should detect when a bug has resulted in an improper chess board.

Example:
The following dictionary would pass because it has one black king and one white king.
{'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen',
'3e': 'wking'}
But this dictionary would fail because it has two white queens:
{'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen',
'3e': 'wqueen'}
"""


def isValidChessBoard(board):
    # check if there is only one black king and one white king
    if sum(value == "bking" for value in board.values()) != 1:
        return False
    if sum(value == "wking" for value in board.values()) != 1:
        return False

    # check if each player has at most 16 pieces
    if sum(value.startswith("b") for value in board.values()) > 16:
        return False
    if sum(value.startswith("w") for value in board.values()) > 16:
        return False

    # check if each player has at most 8 pawns
    if sum(value == "bpawn" for value in board.values()) > 8:
        return False
    if sum(value == "wpawn" for value in board.values()) > 8:
        return False

    # check if all pieces are on a valid space from '1a' to '8h'
    for key in board.keys():
        if not (key[0] in "12345678" and key[1] in "abcdefgh"):
            return False

    return True


# Testing with an valid chess board
theBoard = {
    "1h": "bking",
    "6c": "wqueen",
    "2g": "bbishop",
    "5h": "bqueen",
    "3e": "wking",
}
print(isValidChessBoard(theBoard))  # True
# Testing with an invalid chess board
theBoard = {
    "1h": "bking",
    "6c": "wqueen",
    "2g": "bbishop",
    "5h": "bqueen",
    "3e": "wqueen",
}
print(isValidChessBoard(theBoard))  # False
