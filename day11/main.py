from collections import defaultdict
import functools
lines = []
with open('input.txt', 'r') as file:
    for line in file:
        if '\n' in line:
            lines.append(line[:-1])
        else:
            lines.append(line)
originalStones = [int(x) for x in lines[0].split()]


@functools.lru_cache
def transformStone(num):
    if num == 0:
        return [1]
    if len(str(num)) % 2 == 0:
        return [int(str(num)[0:(len(str(num))//2)]), int(str(num)[len(str(num))//2:])]
    return [num*2024]


def transformStones(blinks):
    stoneDict = {}
    for num in originalStones:
        stoneDict.update({num: 1})
    for _ in range(blinks):
        newStones = defaultdict(int)
        for num, count in stoneDict.items():
            transformedStones = transformStone(num)
            for stone in transformedStones:
                newStones[stone] += count
        stoneDict = newStones
    sum = 0
    for num, count in stoneDict.items():
        sum += count
    print(sum)


def p1():
    transformStones(25)


def p2():
    transformStones(75)


p1()
p2()
