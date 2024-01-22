import random, copy, time

WIDTH, HEIGHT = 60, 20

nextCells = []
for x in range(WIDTH):
    column = []
    for y in range(HEIGHT):
        if random.randint(0, 1):
            column.append("#")  # Add a living cell
        else:
            column.append(" ")  # Add a dead sell
    nextCells.append(column)  # nextCells is a list of column lists

while True:
    print("\n\n\n\n\n")
    currentCells = copy.deepcopy(nextCells)
    for x in range(WIDTH):
        for y in range(HEIGHT):
            print(currentCells[x][y], end="")
        print()

    # Calculate the next step's cells based on current step'scells:
    for x in range(WIDTH):
        for y in range(HEIGHT):
            # Get neighboring coordinates:
            leftCoord = (x - 1) % WIDTH
            rightCoord = (x + 1) % WIDTH
            aboveCoord = (y - 1) % HEIGHT
            belowCoord = (y + 1) % HEIGHT

            # Count number of living neighbors:
            numNeighbors = 0
            if currentCells[leftCoord][aboveCoord] == "#":
                numNeighbors += 1  # top-left
            if currentCells[x][aboveCoord] == "#":
                numNeighbors += 1  # top
            if currentCells[rightCoord][aboveCoord] == "#":
                numNeighbors += 1  # top-right
            if currentCells[leftCoord][y] == "#":
                numNeighbors += 1  # left
            if currentCells[rightCoord][y] == "#":
                numNeighbors += 1  # right
            if currentCells[leftCoord][belowCoord] == "#":
                numNeighbors += 1  # buttom-left
            if currentCells[rightCoord][belowCoord] == "#":
                numNeighbors = +1  # buttom-right

            # set cell
            if currentCells[x][y] == "#" and (numNeighbors == 2 or numNeighbors == 3):
                nextCells[x][y] = "#"  # stay alive
            elif currentCells[x][y] == " " and numNeighbors == 3:
                nextCells[x][y] = "#"  # become alive
            else:
                nextCells[x][y] = " "  # Everything else dies or stays dead.
    time.sleep(1)
