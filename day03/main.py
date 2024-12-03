import re
lines = []
with open('input.txt', 'r') as file:
    for line in file:
        if '\n' in line:
            lines.append(line[:-1])
        else:
            lines.append(line)


def p1():
    pattern = r"mul\(\d+,\d+\)"
    sum = 0
    for line in lines:
        matches = re.findall(pattern, line)
        for match in matches:
            nums = match[4:-1].split(',')
            sum += int(nums[0])*int(nums[1])
    print(sum)


def p2():
    sum = 0
    pattern = r"mul\(\d+,\d+\)|do\(\)|don\'t\(\)"
    do = True
    sum = 0
    for line in lines:
        matches = re.findall(pattern, line)
        for match in matches:
            if match == 'do()':
                do = True
            if match == "don't()":
                do = False
            if do and match != 'do()' and match != "don't()":
                nums = match[4:-1].split(',')
                sum += int(nums[0])*int(nums[1])
    print(sum)


p1()
p2()
