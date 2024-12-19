file = "2024/1/day1.txt"


def file_to_list(file):
    with open(file, "r") as f:
        lines = f.read().strip().splitlines()
        listLeft = []
        listRight = []
        for line in lines:
            x = line.split("   ")
            listLeft.append(int(x[0]))
            listRight.append(int(x[1]))
        return listLeft, listRight


def part1():
    left, right = file_to_list(file)
    n = len(left)
    left.sort()
    right.sort()
    distance = 0
    for i in range(n):
        distance += abs(left[i] - right[i])
    return distance


def part2():
    left, right = file_to_list(file)
    left.sort()
    right.sort()
    n = len(left)
    total = 0
    for i in range(n):
        toCheck = left[i]
        count = 0
        for e in right:
            if e == toCheck:
                count += 1
        total += toCheck * count
    return total


print(part1())
print(part2())
