import re

file = "2024/3/day3.txt"

def file_to_list(file):
    with open(file, "r") as f:
        lines = f.read().strip().splitlines()
    return lines

def checkLine(line):
    listOfAll = re.findall(r"mul\(\d{1,3},\d{1,3}\)", line)
    lineSum = 0
    for e in listOfAll:
        digits = re.findall(r"\d+",e)
        lineSum += int(digits[0]) * int(digits[1])
    return lineSum

def checkLineDo(line, do):
    listOfAll = re.findall(r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)", line)
    lineSum = 0
    do = do
    for e in listOfAll:
        if e == "don't()": 
            do = False
        elif e == "do()":
            do = True
        elif do:
            digits = re.findall(r"\d+",e)
            lineSum += int(digits[0]) * int(digits[1])
    return lineSum , do 

def part1():
    validSum = 0
    for line in file_to_list(file):
        validSum += checkLine(line)
    return validSum

def part2():
    validSum = 0
    do = True
    for line in file_to_list(file):
        validSum += checkLineDo(line, do)[0]
        do = checkLineDo(line, do)[1] 
    return validSum

print(part1())
print(part2())
