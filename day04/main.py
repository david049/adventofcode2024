lines = []
with open('input.txt', 'r') as file:
    for line in file:
        if '\n' in line:
            lines.append(line[:-1])
        else:
            lines.append(line)

charArray = []
for line in lines:
    arr = []
    for char in line:
        arr.append(char)
    charArray.append(line)


def getChar(y, x, deg=False):
    if x < 0 or x >= len(charArray[0]):
        return 'f'
    if y < 0 or y >= len(charArray):
        return 'f'
    if deg:
        print(charArray[y][x])
    return charArray[y][x]


def p1():
    times = 0
    for row in range(len(charArray)):
        for col in range(len(charArray[0])):
            if charArray[row][col] != 'X':
                continue
            # Down
            if getChar(row+1, col) == 'M' and getChar(row+2, col) == "A" and getChar(row+3, col) == "S":
                times += 1
            # Up
            if getChar(row-1, col) == 'M' and getChar(row-2, col) == "A" and getChar(row-3, col) == "S":
                times += 1
            # Right
            if getChar(row, col+1) == 'M' and getChar(row, col+2) == "A" and getChar(row, col+3) == "S":
                times += 1
            # Left
            if getChar(row, col-1) == 'M' and getChar(row, col-2) == "A" and getChar(row, col-3) == "S":
                times += 1
            # Diagonal up left
            if getChar(row-1, col-1) == 'M' and getChar(row-2, col-2) == "A" and getChar(row-3, col-3) == "S":
                times += 1
            # Diagonal up Right
            if getChar(row-1, col+1) == 'M' and getChar(row-2, col+2) == "A" and getChar(row-3, col+3) == "S":
                times += 1
            # Diagonal down left
            if getChar(row+1, col-1) == 'M' and getChar(row+2, col-2) == "A" and getChar(row+3, col-3) == "S":
                times += 1
            # Diagonal down Right
            if getChar(row+1, col+1) == 'M' and getChar(row+2, col+2) == "A" and getChar(row+3, col+3) == "S":
                times += 1
    print(times)


def p2():
    times = 0
    for row in range(len(charArray)):
        for col in range(len(charArray[0])):
            if charArray[row][col] != 'A':
                continue
            if getChar(row-1, col-1) == 'S' and getChar(row+1, col+1) == 'M':
                if getChar(row-1, col+1) == 'S' and getChar(row+1, col-1) == 'M':
                    times += 1
                    continue
            if getChar(row-1, col-1) == 'M' and getChar(row+1, col+1) == 'S':
                if getChar(row-1, col+1) == 'M' and getChar(row+1, col-1) == 'S':
                    times += 1
                    continue
            if getChar(row-1, col-1) == 'M' and getChar(row-1, col+1) == 'M':
                if getChar(row+1, col+1) == 'S' and getChar(row+1, col-1) == 'S':
                    times += 1
                    continue
            if getChar(row-1, col-1) == 'S' and getChar(row-1, col+1) == 'S':
                if getChar(row+1, col+1) == 'M' and getChar(row+1, col-1) == 'M':
                    times += 1
                    continue
            if getChar(row-1, col-1) == 'S' and getChar(row+1, col-1) == 'S':
                if getChar(row-1, col+1) == 'M' and getChar(row+1, col+1) == 'M':
                    times += 1
                    continue
            if getChar(row-1, col-1) == 'M' and getChar(row+1, col-1) == 'M':
                if getChar(row-1, col+1) == 'S' and getChar(row+1, col+1) == 'S':
                    times += 1
                    continue
    print(times)


p1()
p2()
