#! python3
# tablePrinter.py - Prints a table from a list of lists of strings.
"""
Write a function  printTable() that takes a list of lists of strings and displays it
in a well-organized table with each column right-justified.
Assume that all the inner lists will contain the same number of strings.
 
For example, the value could look like this:
tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]
"""


def printTable(tableData):
    colWidths = [0] * len(tableData)

    for i in range(len(tableData)):
        colWidths[i] = len(max(tableData[i], key=len))

    for i in range(len(tableData[0])):
        for j in range(len(tableData)):
            print(tableData[j][i].rjust(colWidths[j]), end=" ")
        print()


# Test the function with the given example.
print("Example usage:")
fruit_data = [
    ["apples", "oranges", "cherries", "banana"],
    ["Alice", "Bob", "Carolgg", "David"],
    ["dogs", "cats", "moose", "geese"],
]
printTable(fruit_data)
