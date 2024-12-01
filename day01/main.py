from collections import defaultdict

lines = []
with open('input.txt', 'r') as file:
    for line in file:
        if '\n' in line:
            lines.append(line[:-1])
        else:
            lines.append(line)

firstnums = []
secondnums = []
for line in lines:
    nums = line.split(" ")
    firstnums.append(int(nums[0]))
    secondnums.append(int(nums[-1]))
firstnums.sort()
secondnums.sort()


def day1():
    differences = 0
    for i in range(len(firstnums)):
        differences += abs(firstnums[i] - secondnums[i])
    print(differences)


def day2():
    occurances = defaultdict(int)
    for num in secondnums:
        occurances[num] = occurances[num] + 1

    score = 0
    for num in firstnums:
        score += num * occurances[num]
    print(score)


day1()
day2()
