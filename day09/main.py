from collections import defaultdict
lines = []
with open('input.txt', 'r') as file:
    for line in file:
        if '\n' in line:
            lines.append(line[:-1])
        else:
            lines.append(line)
fileSums = [int(x) for x in lines[0]]

layout = []
currentId = 0
lookingFile = True
for file in fileSums:
    if lookingFile:
        for i in range(file):
            layout.append(str(currentId))
        currentId += 1
        lookingFile = False
    else:
        for i in range(file):
            layout.append('.')
        lookingFile = True


def p1():
    wholeLayout = layout.copy()
    firstPtr = ''.join(wholeLayout).find('.')
    lastPtr = len(wholeLayout)
    for i in reversed(range(len(wholeLayout))):
        if wholeLayout[i] != '.':
            lastPtr = i
            break
    while firstPtr <= lastPtr:
        if wholeLayout[firstPtr] != '.':
            firstPtr += 1
            continue
        if wholeLayout[lastPtr] == '.':
            lastPtr -= 1
            continue
        wholeLayout[firstPtr], wholeLayout[lastPtr] = wholeLayout[lastPtr], wholeLayout[firstPtr]

    checksum = 0
    for index, file in enumerate(wholeLayout):
        if file == '.':
            break
        checksum += int(file)*index
    print(checksum)


def p2():
    freeSpaceArr = []
    blocksArr = []
    index = 0
    fileIndex = 0
    freeSpace = False
    for file in fileSums:
        if freeSpace:
            freeSpaceArr.append((index, file))
            freeSpace = False
        else:
            blocksArr.append((index, file, fileIndex))
            fileIndex += 1
            freeSpace = True
        index += file
    movedBlocksArr = []
    for i in reversed(range(len(blocksArr))):
        for j in range(len(freeSpaceArr)):
            if freeSpaceArr[j][1] >= blocksArr[i][1] and j < i:
                movedBlocksArr.append(
                    (freeSpaceArr[j][0], blocksArr[i][1], blocksArr[i][2]))
                freeSpaceArr[j] = (
                    freeSpaceArr[j][0] + blocksArr[i][1], freeSpaceArr[j][1] - blocksArr[i][1])
                freeSpaceArr.append((blocksArr[i][0], blocksArr[i][1]))
                blocksArr[i] = (-1, -1, -1)
                break
    freeSpaceArr = sorted(freeSpaceArr, key=lambda x: x[0])
    movedBlocksArr = sorted(movedBlocksArr, key=lambda x: x[0])
    overallSpace = []
    ptrOrig = 0
    ptrMoved = 0
    while ptrOrig < len(blocksArr) or ptrMoved < len(movedBlocksArr):
        if ptrOrig < len(blocksArr) and blocksArr[ptrOrig][0] == -1:
            ptrOrig += 1
            continue
        if ptrMoved >= len(movedBlocksArr) or (ptrOrig < len(blocksArr) and blocksArr[ptrOrig][0] < movedBlocksArr[ptrMoved][0]):
            overallSpace.append(blocksArr[ptrOrig])
            ptrOrig += 1
        else:
            overallSpace.append(movedBlocksArr[ptrMoved])
            ptrMoved += 1
    checksum = 0
    for space in overallSpace:
        index, spaces, id = space
        sum = 0
        for i in range(spaces):
            sum += id * index
            index += 1
        checksum += sum
    print(checksum)


p1()
p2()
