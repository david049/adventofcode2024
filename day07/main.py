lines = []
with open('input.txt', 'r') as file:
    for line in file:
        if '\n' in line:
            lines.append(line[:-1])
        else:
            lines.append(line)


def concat(num1, num2):
    num3str = str(num1) + str(num2)
    return int(num3str)


def p1():
    def operate(result, nums, index, current):
        if current == result and index == len(nums):
            return True
        if index == len(nums):
            return False
        if operate(result, nums, index+1, current*nums[index]):
            return True
        if operate(result, nums, index+1, current+nums[index]):
            return True
        return False

    sum = 0
    for line in lines:
        res, rest = line.split(":")
        result = int(res)
        rest = rest.split(" ")[1:]
        nums = [int(x) for x in rest]
        if operate(result, nums, 1, nums[0]):
            sum += result
    print(sum)


def p2():
    def operate(result, nums, index, current):
        if current == result and index == len(nums):
            return True
        if index == len(nums):
            return False
        if operate(result, nums, index+1, current*nums[index]):
            return True
        if operate(result, nums, index+1, current+nums[index]):
            return True
        if operate(result, nums, index+1, concat(current, nums[index])):
            return True
        return False

    sum = 0
    for line in lines:
        res, rest = line.split(":")
        result = int(res)
        rest = rest.split(" ")[1:]
        nums = [int(x) for x in rest]
        if operate(result, nums, 1, nums[0]):
            sum += result
    print(sum)


p1()
p2()
