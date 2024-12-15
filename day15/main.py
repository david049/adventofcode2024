from copy import deepcopy
lines = []
with open('input.txt', 'r') as file:
    for line in file:
        if '\n' in line:
            lines.append(line[:-1])
        else:
            lines.append(line)
ogBoard = []
moves = []
readingBoard = True
for line in lines:
    if line == '':
        readingBoard = False
        continue
    if readingBoard:
        ogBoard.append([str(x) for x in line])
    else:
        moves.append([str(x) for x in line])


def p1():
    board = deepcopy(ogBoard)
    robotX = -1
    robotY = -1
    for row, line in enumerate(board):
        for col, char in enumerate(line):
            if board[row][col] == '@':
                robotX = col
                robotY = row
                break

    def move(board, row, col, move):
        curMove = (-100, -100)
        if move == '^':
            curMove = (-1, 0)
        if move == '>':
            curMove = (0, 1)
        if move == '<':
            curMove = (0, -1)
        if move == 'v':
            curMove = (1, 0)
        charAtMove = board[row+curMove[0]][col+curMove[1]]
        if charAtMove == '#':
            return row, col
        if charAtMove == '.':
            board[row][col] = '.'
            board[row+curMove[0]][col+curMove[1]] = '@'
            return row+curMove[0], col+curMove[1]
        if charAtMove == 'O':
            curRow = row
            curCol = col
            while True:
                curRow += curMove[0]
                curCol += curMove[1]
                if board[curRow][curCol] == '#':
                    return row, col
                if board[curRow][curCol] == 'O':
                    continue
                if board[curRow][curCol] == '.':
                    break
            while curRow != row or curCol != col:
                newRow, newCol = curRow - curMove[0], curCol - curMove[1]
                board[newRow][newCol], board[curRow][curCol] = board[curRow][curCol], board[newRow][newCol]
                curRow, curCol = newRow, newCol
            return row+curMove[0], col+curMove[1]

    for moveList in moves:
        for rMove in moveList:
            robotY, robotX = move(board, robotY, robotX, rMove)
    sum = 0
    for row, line in enumerate(board):
        for col, char in enumerate(line):
            if board[row][col] == 'O':
                sum += row*100 + col
    print(sum)


def p2():
    board = deepcopy(ogBoard)
    sizedUpBoard = []
    for line in board:
        floorline = []
        for char in line:
            if char == '#':
                floorline += ['#', '#']
            if char == 'O':
                floorline += ['[', ']']
            if char == '.':
                floorline += ['.', '.']
            if char == '@':
                floorline += ['@', '.']
        sizedUpBoard.append(floorline)
    board = sizedUpBoard
    robotX = -1
    robotY = -1
    for row, line in enumerate(board):
        for col, char in enumerate(line):
            if board[row][col] == '@':
                robotX = col
                robotY = row
                break

    def checkAct(row, col, curMove):
        checkRow, checkCol = row + curMove[0], col + curMove[1]
        charAtMove = board[checkRow][checkCol]
        if charAtMove == '.':
            return True
        if charAtMove == '#':
            return False
        if charAtMove == '[':
            return checkAct(checkRow, checkCol, curMove) and checkAct(checkRow, checkCol + 1, curMove)
        else:
            return checkAct(checkRow, checkCol, curMove) and checkAct(checkRow, checkCol - 1, curMove)

    def act(row, col, curMove):
        checkRow, checkCol = row + curMove[0], col + curMove[1]
        charAtMove = board[checkRow][checkCol]
        if charAtMove == '.':
            board[checkRow][checkCol], board[row][col] = board[row][col], board[checkRow][checkCol]
            return
        if charAtMove == '[':
            act(checkRow, checkCol, curMove)
            act(checkRow, checkCol + 1, curMove)
        else:
            act(checkRow, checkCol, curMove)
            act(checkRow, checkCol - 1, curMove)
        board[checkRow][checkCol], board[row][col] = board[row][col], board[checkRow][checkCol]

    def move(board, row, col, move):
        curMove = (-100, -100)
        upDown = False
        if move == '^':
            curMove = (-1, 0)
            upDown = True
        if move == '>':
            curMove = (0, 1)
        if move == '<':
            curMove = (0, -1)
        if move == 'v':
            curMove = (1, 0)
            upDown = True
        charAtMove = board[row+curMove[0]][col+curMove[1]]
        if charAtMove == '#':
            return row, col
        if charAtMove == '.':
            board[row][col] = '.'
            board[row+curMove[0]][col+curMove[1]] = '@'
            return row+curMove[0], col+curMove[1]
        if charAtMove in '[]' and not upDown:
            curRow = row
            curCol = col
            while True:
                curRow += curMove[0]
                curCol += curMove[1]
                if board[curRow][curCol] == '#':
                    return row, col
                if board[curRow][curCol] == '[]':
                    continue
                if board[curRow][curCol] == '.':
                    break
            while curRow != row or curCol != col:
                newRow, newCol = curRow - curMove[0], curCol - curMove[1]
                board[newRow][newCol], board[curRow][curCol] = board[curRow][curCol], board[newRow][newCol]
                curRow, curCol = newRow, newCol
            return row+curMove[0], col+curMove[1]
        if charAtMove in "[]" and upDown:
            if checkAct(row, col, curMove):
                act(row, col, curMove)
                return row + curMove[0], col + curMove[1]
            return row, col
    for moveList in moves:
        for rMove in moveList:
            robotY, robotX = move(board, robotY, robotX, rMove)
    sum = 0
    for row, line in enumerate(board):
        for col, char in enumerate(line):
            if board[row][col] == '[':
                sum += row*100 + col
    print(sum)


p1()
p2()
