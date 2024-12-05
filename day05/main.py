lines = []
with open('input.txt', 'r') as file:
    for line in file:
        if '\n' in line:
            lines.append(line[:-1])
        else:
            lines.append(line)


def getIndex(list, val):
    i = 0
    for num in list:
        if num == val:
            return i
        i += 1
    return -1


def ordered(page, orderings):
    for rule in orderings:
        if rule[0] in page and rule[1] in page:
            index1 = getIndex(page, rule[0])
            index2 = getIndex(page, rule[1])
            if index2 < index1:
                return False
    return True


# P1
pages = []
orderings = []
incorrectPages = []

order = True
for line in lines:
    if line == '':
        order = False
        continue
    if order:
        kvp = line.split('|')
        orderings.append((kvp[0], kvp[1]))

    else:
        pageNums = line.split(',')
        pages.append(pageNums)
sum = 0
for page in pages:
    ruleEnforced = True
    pageOrdered = ordered(page, orderings)
    if pageOrdered:
        sum += int(page[len(page)//2])
    else:
        incorrectPages.append(page)
        continue

print(sum)
# P2
incorrectSum = 0
for page in incorrectPages:
    while not ordered(page, orderings):
        for i in range(len(page)):
            for j in range(i + 1, len(page)):
                if (page[j], page[i]) in orderings:
                    page[i], page[j] = page[j], page[i]
    incorrectSum += int(page[len(page)//2])
print(incorrectSum)
