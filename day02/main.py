lines = []
with open('input.txt', 'r') as file:
    for line in file:
        if '\n' in line:
            lines.append(line[:-1])
        else:
            lines.append(line)


def p1():
    safe = 0
    for line in lines:
        increasing = False
        nums = line.split()
        if int(nums[0]) < int(nums[1]):
            increasing = True
        if abs(int(nums[0])-int(nums[1])) > 3 or abs(int(nums[0])-int(nums[1])) < 1:
            continue
        for i in range(1, len(nums)):
            secondnum = int(nums[i])
            firstnum = int(nums[i-1])
            if abs(secondnum-firstnum) > 3 or abs(secondnum-firstnum) < 1:
                break
            if increasing:
                if secondnum < firstnum:
                    break
            else:
                if secondnum > firstnum:
                    break
            if i == len(nums) - 1:
                safe += 1
    print(safe)


def p2():
    safe = 0
    for line in lines:
        numbers = line.split()
        for j in range(0, len(numbers)):
            nums = numbers.copy()
            lineSafe = 0
            increasing = False
            nums.pop(j)
            if int(nums[0]) < int(nums[1]):
                increasing = True
            if abs(int(nums[0])-int(nums[1])) > 3 or abs(int(nums[0])-int(nums[1])) < 1:
                continue
            for i in range(1, len(nums)):
                secondnum = int(nums[i])
                firstnum = int(nums[i-1])
                if abs(secondnum-firstnum) > 3 or abs(secondnum-firstnum) < 1:
                    break
                if increasing:
                    if secondnum < firstnum:
                        break
                else:
                    if secondnum > firstnum:
                        break
                if i == len(nums) - 1:
                    lineSafe += 1
            if lineSafe > 0:
                safe += 1
                break
    print(safe)


p1()
p2()
