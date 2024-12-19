file = "2024/2/day2.txt"


def file_to_list(file):
    with open(file, "r") as f:
        lines = f.read().strip().splitlines()
    return lines


def checkRow(row):
    row = [int(x) for x in row]
    for i in range(len(row) - 1):
        if 0 == abs(row[i] - row[i + 1]) or abs(row[i] - row[i + 1]) > 3:
            return False
    sortedRow = list(sorted(row))
    if sortedRow != row and sortedRow[::-1] != row:
        return False
    return True

def check_row_with_removals(row, notAllowed):
    if len(notAllowed) == 0:
        return True
    row_copy = list(row)
    for e in notAllowed:
        removed = row_copy.pop(e)
        if checkRow(row_copy):
            return True
        row_copy.insert(e, removed)
    return False
     
def part1():
    validLines = 0
    lines = file_to_list(file)
    for row in lines:
        validLines += checkRow(row.split())
    return validLines


def part2():
    validLines = 0
    lines = file_to_list(file)
    for row in lines:
        row = [int(x) for x in row.split()]
        notAllowed = []
        for i in range(len(row) - 1):
            if 0 == abs(row[i] - row[i + 1]) or abs(row[i] - row[i + 1]) > 3:
                notAllowed.append(i)
                notAllowed.append(i+1)
        sortedRow = list(sorted(row))
        for i in range(len(row)):
            if row[i] != sortedRow[i] and row[i] != sortedRow[::-1][i]:
                notAllowed.append(i)
        validLines += check_row_with_removals(row, notAllowed)
    return validLines


print(part1())
print(part2())
