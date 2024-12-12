from enum import Enum


class Direction(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4


lines = []
with open('input.txt', 'r') as file:
    for line in file:
        if '\n' in line:
            lines.append(line[:-1])
        else:
            lines.append(line)

visited = []
gardenGrid = []
for line in lines:
    visit = [0]*len(line)
    visited.append(visit)
    row = []
    for char in line:
        row.append(char)
    gardenGrid.append(row)


def getChar(y, x, charArray):
    if x < 0 or x >= len(charArray[0]):
        return '#'
    if y < 0 or y >= len(charArray):
        return '#'
    return charArray[y][x]


def getNeighbours(row, col, arr):
    validNeighbours = []
    directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    for direction in directions:
        newRow, newCol = row + direction[0], col + direction[1]
        if getChar(newRow, newCol, arr) == arr[row][col]:
            validNeighbours.append((newRow, newCol))
    return validNeighbours


def getPerimeter(num):
    perimeterByNeighbours = {
        4: 0,
        3: 1,
        2: 2,
        1: 3,
        0: 4
    }
    return perimeterByNeighbours.get(num) if num in perimeterByNeighbours else -1


def dfs(row, col):
    neighbours = getNeighbours(row, col, gardenGrid)
    addedPerimeter = getPerimeter(len(neighbours))
    addedArea = 1
    visited[row][col] = 1
    for neighbour in neighbours:
        if visited[neighbour[0]][neighbour[1]] == 1:
            continue
        result = dfs(neighbour[0], neighbour[1])
        addedPerimeter += result[0]
        addedArea += result[1]
    return addedPerimeter, addedArea


def p1():
    regions = []
    for row, line in enumerate(gardenGrid):
        for col, _ in enumerate(line):
            if visited[row][col] == 0:
                perimeter, area = dfs(row, col)
                regions.append((perimeter, area))
    sum = 0
    for region in regions:
        sum += region[0]*region[1]
    print(sum)


def getNeighboursP2(row, col, arr):
    validNeighbours = []
    validDirections = []
    directions = [(-1, 0, Direction.UP), (1, 0, Direction.DOWN),
                  (0, 1, Direction.RIGHT), (0, -1, Direction.LEFT)]
    for direction in directions:
        newRow, newCol = row + direction[0], col + direction[1]
        if getChar(newRow, newCol, arr) == arr[row][col]:
            validNeighbours.append((newRow, newCol))
            validDirections.append(direction[2])
    return validNeighbours, validDirections


def getNumCorners(directions, char, row, col):
    if len(directions) == 0:
        return 4
    if len(directions) == 1:
        return 2
    if len(directions) == 2:
        if Direction.UP in directions and Direction.DOWN in directions:
            return 0
        if Direction.LEFT in directions and Direction.RIGHT in directions:
            return 0
        if Direction.UP in directions and Direction.LEFT in directions:
            if gardenGrid[row-1][col-1] != char:
                return 2
            return 1
        if Direction.UP in directions and Direction.RIGHT in directions:
            if gardenGrid[row-1][col+1] != char:
                return 2
            return 1
        if Direction.DOWN in directions and Direction.LEFT in directions:
            if gardenGrid[row+1][col-1] != char:
                return 2
            return 1
        if Direction.DOWN in directions and Direction.RIGHT in directions:
            if gardenGrid[row+1][col+1] != char:
                return 2
            return 1
        return 1
    if len(directions) == 3:
        if Direction.DOWN not in directions:
            corners = 0
            if gardenGrid[row-1][col-1] != char:
                corners += 1
            if gardenGrid[row-1][col+1] != char:
                corners += 1
        if Direction.UP not in directions:
            corners = 0
            if gardenGrid[row+1][col-1] != char:
                corners += 1
            if gardenGrid[row+1][col+1] != char:
                corners += 1
        if Direction.LEFT not in directions:
            corners = 0
            if gardenGrid[row-1][col+1] != char:
                corners += 1
            if gardenGrid[row+1][col+1] != char:
                corners += 1
        if Direction.RIGHT not in directions:
            corners = 0
            if gardenGrid[row-1][col-1] != char:
                corners += 1
            if gardenGrid[row+1][col-1] != char:
                corners += 1
        return corners
    if len(directions) == 4:
        corners = 0
        if gardenGrid[row-1][col-1] != char:
            corners += 1
        if gardenGrid[row-1][col+1] != char:
            corners += 1
        if gardenGrid[row+1][col-1] != char:
            corners += 1
        if gardenGrid[row+1][col+1] != char:
            corners += 1
        return corners
    print("illegal case")
    return -1


def dfsp2(row, col):
    neighbours, directions = getNeighboursP2(row, col, gardenGrid)
    addedArea = 1
    corners = getNumCorners(directions, gardenGrid[row][col], row, col)
    visited[row][col] = 2
    for neighbour in neighbours:
        if visited[neighbour[0]][neighbour[1]] == 2:
            continue
        result = dfsp2(neighbour[0], neighbour[1])
        addedArea += result[0]
        corners += result[1]
    return addedArea, corners


def p2():
    regions = []
    for row, line in enumerate(gardenGrid):
        for col, _ in enumerate(line):
            if visited[row][col] == 1:
                area, corners = dfsp2(row, col)
                regions.append((area, corners))
    sum = 0
    for region in regions:
        sum += region[0]*region[1]
    print(sum)


p1()
p2()
