"""
Character Picture Grid
Say you have a list of lists where each value in the inner lists is a one-character string, like this:
[["a", "b"], ["c", "d"]]
Write a function that takes a list of lists of strings and displays it in a well-organized table
with each column right-justified.
Assume that all the inner lists will contain the same number of strings. For example,
the value could look like this:
grid = [[".", ".", ".", ".", ".", "."],
        [".", "O", "O", ".", ".", "."],
        ["O", "O", "O", "O", ".", "."],
        ["O", "O", "O", "O", "O", "."],
        [".", "O", "O", "O", "O", "O"],
        ["O", "O", "O", "O", "O", "."],
        ["O", "O", "O", "O", ".", "."],
        [".", "O", "O", ".", ".", "."],
        [".", ".", ".", ".", ".", "."]]
Your code would print this picture:
..OO.OO..
.OOOOOOO.
.OOOOOOO.
..OOOOO..
...OOO...
....O....
"""

grid = [
    [".", ".", ".", ".", ".", "."],
    [".", "O", "O", ".", ".", "."],
    ["O", "O", "O", "O", ".", "."],
    ["O", "O", "O", "O", "O", "."],
    [".", "O", "O", "O", "O", "O"],
    ["O", "O", "O", "O", "O", "."],
    ["O", "O", "O", "O", ".", "."],
    [".", "O", "O", ".", ".", "."],
    [".", ".", ".", ".", ".", "."],
]


def display_picture(grid):
    for i in range(len(grid[0])):
        for j in range(len(grid)):
            print(grid[j][i], end="")
        print("")


display_picture(grid)
