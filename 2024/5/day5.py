from collections import defaultdict

input = "2024/5/day5.txt"

def getInput(file):
    with open(file, "r") as f:
        lines = f.read().rstrip().split("\n")
        rules = []
        updates = []
        flag = False
        for line in lines:
            if not line:
                flag = True
            elif flag:
                updates.append(line)
            else:
                rules.append(line)
    return rules, updates

def par1():
    before = defaultdict(set)
    rules , updates = getInput(input)
    middleNumbers = []
    wrongNumbers = []
    for e in rules:
        rule = e.split("|")
        before[rule[0]].add(rule[1])
    for line in updates:
        checked = set()
        numbers = line.split(",")
        flag = True
        for number in numbers:
            if len(checked.intersection(before[number])) > 0:
                flag = False
            checked.add(number)
        if flag:
            middleNumbers.append(numbers[len(numbers)//2])
        if not flag:
            wrongNumbers.append(numbers)
    middleNumbers = [int(x) for x in middleNumbers]
    return sum(middleNumbers) , wrongNumbers , before

def par2():
    middleNumbers = []
    toFix, before = par1()[1], par1()[2]
    for wrongLine in toFix:
        perfect = []
        for number in list(wrongLine):
            elements = set(perfect).intersection(before[number])
            if len(elements) > 1:
                index = []
                for element in elements:
                    index.append(perfect.index(element))
                minIndex = min(index)
                perfect.insert(minIndex , number)
            elif len(elements) == 1:
                perfect.insert(perfect.index(elements.pop()) , number)
            else:
                perfect.append(number)
        middleNumbers.append(perfect[len(perfect)//2])
    middleNumbers = [int(x) for x in middleNumbers]
    return sum(middleNumbers)

print(par1()[0])
print(par2())

