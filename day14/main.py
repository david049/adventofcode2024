import re
lines = []
with open('input.txt', 'r') as file:
    for line in file:
        if '\n' in line:
            lines.append(line[:-1])
        else:
            lines.append(line)
pattern = r"-?\d+"
robots = []
for line in lines:
    matches = re.findall(pattern, line)
    robots.append([int(x) for x in matches])
WIDTH = 101
HEIGHT = 103
SECONDS = 100 * 100


def moveRobot(robot):
    px, py, vx, vy = robot[0], robot[1], robot[2], robot[3]
    px += vx
    py += vy
    if py >= HEIGHT:
        py = py % HEIGHT
    if py < 0:
        py = HEIGHT + py
    if px >= WIDTH:
        px = px % WIDTH
    if px < 0:
        px = WIDTH + px
    return [px, py, vx, vy]


def hasSusRow(bathroom):
    for row in bathroom:
        count = 0
        for char in row:
            if char > 0:
                count += 1
                if count > 9:
                    return True
            else:
                count = 0
    return False


def printMapIfSus(robots, seconds):
    bathroom = []
    for i in range(HEIGHT):
        bathroom.append([0]*WIDTH)
    for robot in robots:
        bathroom[robot[1]][robot[0]] += 1
    if hasSusRow(bathroom):
        print(seconds + 1)
        for line in bathroom:
            print(''.join(str(x) for x in line))


def countInQuadrant(robots):
    midpointHeight = HEIGHT//2
    midpointWidth = WIDTH//2
    q1, q2, q3, q4 = 0, 0, 0, 0
    for robot in robots:
        rx, ry = robot[0], robot[1]
        if rx < midpointWidth:
            if ry < midpointHeight:
                q1 += 1
            if ry > midpointHeight:
                q2 += 1
        if rx > midpointWidth:
            if ry < midpointHeight:
                q3 += 1
            if ry > midpointHeight:
                q4 += 1
    return q1 * q2 * q3 * q4


for i in range(SECONDS):
    newRobots = []
    for robot in robots:
        newRobots.append(moveRobot(robot))
    robots = newRobots
    printMapIfSus(robots, i)
    if i == 99:
        print(countInQuadrant(robots))
