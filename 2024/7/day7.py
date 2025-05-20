import itertools
import time

file = "2024/7/7.txt"


def file_to_list(file):
    with open(file, "r") as f:
        lines = f.read().strip().splitlines()
    return lines


def part1():
    operators = "+*"
    allNumbers = []
    goodNumbers = 0
    for line in file_to_list(file):
        numbers = [int("".join(filter(str.isdigit, x))) for x in line.split()]
        allNumbers.append(numbers)
    for test in allNumbers:
        goal = test[0]
        combinations = itertools.product(operators, repeat=len(test) - 2)
        for combination in combinations:
            flag = False
            for operator in combination:
                summedUp = test[1]
                length = len(combination)
                for i in range(length):
                    if combination[i] == "+":
                        summedUp += test[i + 2]
                    else:
                        summedUp *= test[i + 2]
                if summedUp == goal:
                    flag = True
            if flag:
                goodNumbers += goal
                flag = False
                break
    return goodNumbers


def part2():
    operators = "+*|"
    allNumbers = []
    goodNumbers = 0
    for line in file_to_list(file):
        numbers = [int("".join(filter(str.isdigit, x))) for x in line.split()]
        allNumbers.append(numbers)
    for test in allNumbers:
        goal = test[0]
        combinations = itertools.product(operators, repeat=len(test) - 2)
        for combination in combinations:
            summedUp = test[1]
            length = len(combination)
            for i in range(length):
                if combination[i] == "+":
                    summedUp += test[i + 2]
                elif combination[i] == "|":
                    summedUp = int(str(summedUp) + str(test[i + 2]))
                else:
                    summedUp *= test[i + 2]
            if summedUp == goal:
                goodNumbers += goal
                break
    return goodNumbers


start = time.perf_counter()
print(part1())
print(part2())
print(time.perf_counter() - start)
