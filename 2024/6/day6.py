input = "2024/6/6.txt"


def getInput(file):
    with open(file, "r") as f:
        lines = f.read().rstrip().split("\n")
        grid = []
        for line in lines:
            line.rstrip()
            grid.append([letter for letter in line])
    return grid


def part1():
    grid = getInput(input)
    guard = ["<", "^", ">", "v"]
    for row in range(len(grid)):
        for coloum in range(len(grid[row])):
            if grid[row][coloum] in guard:
                faced, x, y = grid[row][coloum], coloum, row
                grid[y][x] = 1
    while True:
        try:
            if faced == "<":
                if grid[y][x - 1] == "#":
                    faced = "^"
                else:
                    x -= 1
                    grid[y][x] = 1
            if faced == "^":
                if grid[y - 1][x] == "#":
                    faced = ">"
                else:
                    y -= 1
                    grid[y][x] = 1
            if faced == ">":
                if grid[y][x + 1] == "#":
                    faced = "v"
                else:
                    x += 1
                    grid[y][x] = 1
            if faced == "v":
                if grid[y + 1][x] == "#":
                    faced = "<"
                else:
                    y += 1
                    grid[y][x] = 1
        except IndexError:
            break
    total = 0
    for line in grid:
        total += line.count(1)
    return total

def leadToOldPath(grid, x, y, faced):
    while True:
        try:
            if faced == "<":
                if grid[y - 1][x] == "|":
                    return True
                y += 1
            if faced == "^":
                if grid[y][x +1] == "-":
                    return True
                x += 1
            if faced == ">":
                if grid[y + 1][x] == "|":
                    return True
                y -= 1
            if faced == "v":
                if grid[y][x - 1] == "-":
                    return True
                x -= 1
        except IndexError:
            return False


def part2():
    grid = getInput(input)
    guard = ["<", "^", ">", "v"]
    for row in range(len(grid)):
        for coloum in range(len(grid[row])):
            if grid[row][coloum] in guard:
                faced, x, y = grid[row][coloum], coloum, row
                grid[y][x] = 1
    marked = []
    while True:
        try:
            if faced == "<":
                if leadToOldPath(grid, x, y, faced) and not grid[y + 1][x] == "#":
                    marked.append((x-1, y))
                if grid[y][x - 1] == "#":
                    faced = "^"
                else:
                    x -= 1
                    if grid[y][x] == ".":
                        grid[y][x] = "-"
                    elif grid[y][x] == "|" or "-":
                        grid[y][x] = "+"
            if faced == "^":
                if leadToOldPath(grid, x, y, faced) and (not grid[y][x - 1] == "#"):
                    marked.append((x, y +1))
                if grid[y - 1][x] == "#":
                    faced = ">"
                else:
                    y -= 1
                    if grid[y][x] == ".":
                        grid[y][x] = "|"
                    elif grid[y][x] == "|" or "-":
                        grid[y][x] = "+"
            if faced == ">":
                if leadToOldPath(grid, x, y, faced) and (not grid[y - 1][x] == "#"):
                    marked.append((x+1, y))
                if grid[y][x + 1] == "#":
                    faced = "v"
                else:
                    x += 1
                    if grid[y][x] == ".":
                        grid[y][x] = "-"
                    elif grid[y][x] == "|" or "-":
                        grid[y][x] = "+"
            if faced == "v":
                if leadToOldPath(grid, x, y, faced) and not grid[y][x + 1] == "#":
                    marked.append((x, y + 1))
                if grid[y + 1][x] == "#":
                    faced = "<"
                else:
                    y += 1
                    if grid[y][x] == ".":
                        grid[y][x] = "|"
                    elif grid[y][x] == "|" or "-":
                        grid[y][x] = "+"
        except IndexError:
            break
    return len(set(marked))


print(part1())
print(part2())
