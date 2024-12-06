from collections import defaultdict

lines = []
with open('input.txt', 'r') as file:
    for line in file:
        if '\n' in line:
            lines.append(line[:-1])
        else:
            lines.append(line)


def getChar(y, x, charArray):
    if x < 0 or x >= len(charArray[0]):
        return 'z'
    if y < 0 or y >= len(charArray):
        return 'z'
    return charArray[y][x]


def copyArray(arr):
    newArray = []
    for line in arr:
        newArray.append(list(line))
    return newArray


directions = {
    '^': (0, -1),
    '>': (1, 0),
    'v': (0, 1),
    '<': (-1, 0)
}
newDirection = {
    '^': '>',
    '>': 'v',
    'v': '<',
    '<': '^'
}

arr = []
visitedArray = []
startx, starty = 0, 0
cury = 0
for line in lines:
    curx = 0
    arrLine = []
    for char in line:
        arrLine.append(char)
        if char == '^':
            startx, starty = curx, cury
        curx += 1
    visitedArray.append(['o']*len(line))
    arr.append(list(line))
    cury += 1


def p1():
    newSquares = 0
    charArray = copyArray(arr)
    for line in charArray:
        line = list(line)
    currentX, currentY = startx, starty
    while True:
        if visitedArray[currentY][currentX] == 'o':
            visitedArray[currentY][currentX] = 'x'
            newSquares += 1
        newX, newY = directions[charArray[currentY][currentX]]
        if getChar(currentY + newY, currentX + newX, charArray) == 'z':
            if visitedArray[currentY][currentX] == 'o':
                visitedArray[currentY][currentX] = 'x'
                newSquares += 1
            break
        if getChar(currentY + newY, currentX + newX, charArray) == '#':
            newDir = newDirection[charArray[currentY][currentX]]
            charArray[currentY][currentX] = newDir
            continue
        char = charArray[currentY][currentX]
        charArray[currentY+newY][currentX+newX] = char
        charArray[currentY][currentX] = '.'
        currentX += newX
        currentY += newY
    print(newSquares)


def p2():
    loops = 0
    for y in range(len(arr)):
        for x in range(len(arr[0])):
            if getChar(y, x, arr) == '#' or getChar(y, x, arr) == '^':
                continue
            charArray = copyArray(arr)
            charArray[y][x] = '#'
            visitedStates = defaultdict(int)
            currentX, currentY = startx, starty
            currentState = (currentX, currentY, charArray[currentY][currentX])
            visitedStates[currentState] = '1'
            while True:
                if visitedArray[currentY][currentX] == 'o':
                    visitedArray[currentY][currentX] = 'x'
                newX, newY = directions[charArray[currentY][currentX]]
                if getChar(currentY + newY, currentX + newX, charArray) == 'z':
                    break
                if getChar(currentY + newY, currentX + newX, charArray) == '#':
                    newDir = newDirection[charArray[currentY][currentX]]
                    charArray[currentY][currentX] = newDir
                    continue
                char = charArray[currentY][currentX]
                charArray[currentY+newY][currentX+newX] = char
                charArray[currentY][currentX] = '.'
                currentX += newX
                currentY += newY
                if visitedStates[(currentX, currentY,  charArray[currentY][currentX])] == 1:
                    loops += 1
                    break
                visitedStates[(currentX, currentY,
                               charArray[currentY][currentX])] = 1
    print(loops)


p1()
p2()
