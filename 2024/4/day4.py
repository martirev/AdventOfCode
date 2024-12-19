input = "2024/4/day4.txt"

def getInput(file):
    with open(file, "r") as f:
        lines = f.read().rstrip().split("\n")
        grid = []
        for line in lines:
            line.rstrip()
            grid.append([letter for letter in line])
    return grid

def part1():
    count = 0
    word = "XMAS"
    grid = getInput(input)
    maxRow = len(grid)
    maxColumn = len(grid[0])
    indexses = []
    for y in range(maxRow):
        for x in range(maxColumn):
            if x - 3 >= 0:
                toCheck = "".join(grid[y][x -3: x + 1][::-1])
                if toCheck == word:
                    count += 1
                    indexses.append((x,y))
            if x + 3 <= maxColumn:
                toCheck = "".join(grid[y][x:x + 4])
                if toCheck == word:
                    count += 1
                    indexses.append((x,y))
            if y - 3 >= 0:
                toCheck = "".join(grid[y][x] + grid[y - 1][x] + grid[y - 2][x] + grid[y - 3][x])
                if toCheck == word:
                    count += 1
                    indexses.append((x,y))
            if y + 3 < maxRow:
                toCheck = "".join(grid[y][x] + grid[y + 1][x] + grid[y + 2][x] + grid[y + 3][x])
                if toCheck == word:
                    count += 1
                    indexses.append((x,y))
            if x - 3 >= 0 and y - 3 >= 0:
                toCheck = "".join(grid[y][x] + grid[y - 1][x - 1] + grid[y - 2][x - 2] + grid[y - 3][x - 3])
                if toCheck == word:
                    count += 1
                    indexses.append((x,y))
            if x + 3 < maxColumn and y - 3 >= 0:
                toCheck = "".join(grid[y][x] + grid[y - 1][x + 1] + grid[y - 2][x + 2] + grid[y - 3][x + 3])
                if toCheck == word:
                    count += 1
                    indexses.append((x,y))
            if x - 3 >= 0 and y + 3 < maxRow:
                toCheck = "".join(grid[y][x] + grid[y + 1][x - 1] + grid[y + 2][x - 2] + grid[y + 3][x - 3])
                if toCheck == word:
                    count += 1
                    indexses.append((x,y))
            if x + 3 < maxColumn and y + 3 < maxRow:
                toCheck = "".join(grid[y][x] + grid[y + 1][x + 1] + grid[y + 2][x + 2] + grid[y + 3][x + 3])
                if toCheck == word:
                    count += 1
                    indexses.append((x,y))
    return count

def part2():
    count = 0
    word = "MAS"
    grid = getInput(input)
    maxRow = len(grid)
    maxColumn = len(grid[0])
    indexses = []
    for y in range(1 , maxRow - 1):
        for x in range(1 ,maxColumn - 1):
            word1 = "".join(grid[y - 1][x - 1] + grid[y][x] + grid[y + 1][x + 1])
            word2 = "".join(grid[y - 1][x + 1] + grid[y][x] + grid[y + 1][x - 1])
            if (word1 == word or word1[::-1] == word) and (word2 == word or word2[::-1] == word):
                count += 1
                indexses.append((x,y))
    return count


print(part1())
print(part2())


