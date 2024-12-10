lines = []
with open('input.txt', 'r') as file:
    for line in file:
        if '\n' in line:
            lines.append(line[:-1])
        else:
            lines.append(line)
grid = []
zeros = []
for row, line in enumerate(lines):
    addRow = []
    for col, char in enumerate(line):
        addRow.append(int(char))
        if char == '0':
            zeros.append((row, col))
    grid.append(addRow)


def getNum(row, col, arr):
    if col < 0 or col >= len(arr[0]):
        return 100
    if row < 0 or row >= len(arr):
        return 100
    return arr[row][col]


def getNeighbours(row, col, arr):
    validNeighbours = []
    directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    for direction in directions:
        newRow, newCol = row + direction[0], col + direction[1]
        if getNum(newRow, newCol, arr) == arr[row][col] + 1:
            validNeighbours.append((newRow, newCol))
    return validNeighbours


def findNinesP1(row, col, arr, visited):
    if (row, col) in visited:
        return 0
    visited.add((row, col))
    if arr[row][col] == 9:
        return 1
    neighbours = getNeighbours(row, col, arr)
    if len(neighbours) == 0:
        return 0
    sumNines = 0
    for neighbour in neighbours:
        sumNines += findNinesP1(neighbour[0], neighbour[1], arr, visited)
    return sumNines


def findNinesP2(row, col, arr):
    if arr[row][col] == 9:
        return 1
    neighbours = getNeighbours(row, col, arr)
    if len(neighbours) == 0:
        return 0
    sumNines = 0
    for neighbour in neighbours:
        sumNines += findNinesP2(neighbour[0], neighbour[1], arr)
    return sumNines


def p1():
    sum = 0
    for zero in zeros:
        sum += findNinesP1(zero[0], zero[1], grid, set())
    print(sum)


def p2():
    sum = 0
    for zero in zeros:
        sum += findNinesP2(zero[0], zero[1], grid)
    print(sum)


p1()
p2()
