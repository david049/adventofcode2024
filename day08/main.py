from collections import defaultdict
lines = []
with open('input.txt', 'r') as file:
    for line in file:
        if '\n' in line:
            lines.append(line[:-1])
        else:
            lines.append(line)


def getDist(a, b):
    ay, ax = a[0], a[1]
    by, bx = b[0], b[1]
    return ay-by, ax-bx


def inRange(row, col):
    if row >= len(lines) or row < 0:
        return False
    if col >= len(lines[0]) or col < 0:
        return False
    return True


characterLocations = defaultdict(list)
characters = set()
for row, line in enumerate(lines):
    for col, char in enumerate(line):
        if char != '.':
            characterLocations[char].append((row, col))
            characters.add(char)


def p1():
    validLocations = set()

    for character in characters:
        locations = characterLocations[character]
        for i in range(len(locations)):
            for j in range(i + 1, len(locations)):
                distRow, distCol = getDist(locations[j], locations[i])
                if inRange(locations[j][0] + distRow, locations[j][1] + distCol):
                    validLocations.add(
                        (locations[j][0] + distRow, locations[j][1] + distCol))

                if inRange(locations[i][0]-distRow, locations[i][1]-distCol):
                    validLocations.add(
                        (locations[i][0]-distRow, locations[i][1]-distCol))
    print(len(validLocations))


def p2():
    validLocations = set()

    for character in characters:
        locations = characterLocations[character]
        for i in range(len(locations)):
            for j in range(i + 1, len(locations)):
                distRow, distCol = getDist(locations[j], locations[i])
                location1 = locations[j]
                while inRange(location1[0], location1[1]):
                    validLocations.add((location1[0], location1[1]))
                    location1 = location1[0] + distRow, location1[1] + distCol

                location2 = locations[i]
                while inRange(location2[0], location2[1]):
                    validLocations.add((location2[0], location2[1]))
                    location2 = location2[0]-distRow, location2[1]-distCol
    print(len(validLocations))


p1()
p2()
