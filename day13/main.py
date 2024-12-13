import re
import heapq
import z3

lines = []
with open('input.txt', 'r') as file:
    for line in file:
        if '\n' in line:
            lines.append(line[:-1])
        else:
            lines.append(line)

games = []
pattern = r"(\d+).*?(\d+)"
for line in lines:
    if 'A' in line:
        a = re.findall(pattern, line)[0]
        a = (int(a[0]), int(a[1]))
    if 'B' in line:
        b = re.findall(pattern, line)[0]
        b = (int(b[0]), int(b[1]))
    if 'Prize' in line:
        p = re.findall(pattern, line)[0]
        p = (int(p[0]), int(p[1]))
    if line == '':
        games.append((a, b, p))


def p1():
    def findLeastCost(game):
        a, b, prize = game
        minHeap = []
        states = set()
        heapq.heappush(minHeap, (3, a[0], a[1]))
        heapq.heappush(minHeap, (1, b[0], b[1]))
        while len(minHeap) > 0:
            cost, x, y = heapq.heappop(minHeap)
            if (cost, x, y) in states:
                continue
            states.add((cost, x, y))
            if x > prize[0]:
                continue
            if y > prize[1]:
                continue
            if x == prize[0] and y == prize[1]:
                return cost
            if (cost+3, x+a[0], y+a[1]) not in states:
                heapq.heappush(minHeap, (cost+3, x+a[0], y+a[1]))
            if (cost+1, x+b[0], y+b[1]) not in states:
                heapq.heappush(minHeap, (cost+1, x+b[0], y+b[1]))
        return 0

    sum = 0
    for game in games:
        sum += (findLeastCost(game))
    print(sum)


def p2():
    sum = 0
    for game in games:
        a, b, prize = game
        x = z3.Int('x')
        y = z3.Int('y')
        solver = z3.Solver()
        solver.add(a[0] * x + b[0] * y == (prize[0] + 10000000000000))
        solver.add(a[1] * x + b[1] * y == (prize[1] + 10000000000000))

        if solver.check() == z3.sat:
            model = solver.model()
            sum += model[x].as_long()*3 + model[y].as_long()
    print(sum)


p1()
p2()
