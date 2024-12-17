from collections import defaultdict
from enum import Enum
import heapq


class Direction(Enum):
    NORTH = 1
    SOUTH = 2
    WEST = 3
    EAST = 4

    def __lt__(self, other):
        return self.value < other.value


lines = []
with open('input.txt', 'r') as file:
    for line in file:
        if '\n' in line:
            lines.append(line[:-1])
        else:
            lines.append(line)
board = []
for line in lines:
    board.append([str(x) for x in line])

startrow = -1
startcol = -1
endrow = -1
endcol = -1
for row, line in enumerate(board):
    for col, char in enumerate(line):
        if char == 'E':
            endrow = row
            endcol = col
        if char == 'S':
            startrow = row
            startcol = col
    if endrow >= 0 and startrow >= 0:
        break


def getNeighbours(row, col):
    validNeighbours = []
    directions = [(-1, 0, Direction.NORTH), (1, 0, Direction.SOUTH),
                  (0, 1, Direction.EAST), (0, -1, Direction.WEST)]
    for direction in directions:
        newRow, newCol = row + direction[0], col + direction[1]
        if board[newRow][newCol] == '.' or board[newRow][newCol] == "E" or board[newRow][newCol] == 'S':
            validNeighbours.append((newRow, newCol, direction[2]))
    return validNeighbours


def getRotationCost(curDir, newDir):
    if curDir == newDir:
        return 0
    if curDir == Direction.NORTH or curDir == Direction.SOUTH:
        if newDir == Direction.EAST or newDir == Direction.WEST:
            return 1000
        return 2000
    if curDir == Direction.EAST or curDir == Direction.WEST:
        if newDir == Direction.NORTH or newDir == Direction.SOUTH:
            return 1000
        return 2000
    print("this case shouldn't happen", curDir, newDir)
    return -1


def djikstra(startrow, startcol, endrow, endcol, startDir, dict):
    heap = []
    heapq.heappush(heap, (0, startrow, startcol, startDir))
    steps = 0
    visited = set()
    while len(heap) > 0:
        steps += 1
        cost, row, col, direction = heapq.heappop(heap)
        if (row, col, direction) in visited:
            continue
        if cost < dict[(row, col)]:
            dict[(row, col)] = cost
        visited.add((row, col, direction))
        if row == endrow and col == endcol:
            return cost
        neighbours = getNeighbours(row, col)
        for neighbour in neighbours:
            nRow, nCol, nDir = neighbour
            heapq.heappush(
                heap, (cost+getRotationCost(direction, nDir) + 1, nRow, nCol, nDir))
    return -1


forwardDict = defaultdict(lambda: float('inf'))
backwardDict = defaultdict(lambda: float('inf'))
costp1 = djikstra(startrow, startcol, endrow, endcol,
                  Direction.EAST, forwardDict)
print(costp1)

costp2 = djikstra(endrow, endcol, startrow, startcol,
                  Direction.SOUTH, backwardDict)

seats = set()
for row in range(len(lines)):
    for col in range(len(lines[0])):
        costforward = forwardDict[(row, col)]
        costbackward = backwardDict[(row, col)]
        # TODO some day: figure out why some are 1000 off.
        if costforward + costbackward == costp1 or costforward + costbackward + 1000 == costp1:
            seats.add((row, col))
            board[row][col] = "O"
print(len(seats))
