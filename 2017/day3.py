from collections import defaultdict
import itertools


puzzleInput = 325489


def part1():
    current = 1
    movingDirection = "r"
    grid = defaultdict(lambda: 0)
    grid[(0, 0)] = current
    grid[(1, 0)] = current
    x, y = 1, 0
    while current < puzzleInput:
        if movingDirection == "r":
            if grid[(x, y + 1)] == 0:
                movingDirection = "u"
                x, y = x, y + 1
            else:
                x, y = x + 1, y
        elif movingDirection == "u":
            if grid[(x - 1, y)] == 0:
                movingDirection = "l"
                x, y = x - 1, y 
            else:
                x, y = x, y + 1
        elif movingDirection == "l":
            if grid[(x, y - 1)] == 0:
                movingDirection = "d"
                x, y = x, y - 1
            else:
                x, y = x - 1, y
        else:
            if grid[(x + 1 , y)] == 0:
                movingDirection = "r"
                x, y = x + 1, y
            else:
                x, y = x, y - 1
        grid[(x,y)] = current
        current += 1 
    return abs(x) + abs(y) + 1


def part2():
    current = 1
    movingDirection = "r"
    grid = defaultdict(lambda: 0)
    grid[(0, 0)] = current
    grid[(1, 0)] = current
    x, y = 1, 0
    while current < puzzleInput:
        if movingDirection == "r":
            if grid[(x, y + 1)] == 0:
                movingDirection = "u"
                x, y = x, y + 1
            else:
                x, y = x + 1, y
        elif movingDirection == "u":
            if grid[(x - 1, y)] == 0:
                movingDirection = "l"
                x, y = x - 1, y 
            else:
                x, y = x, y + 1
        elif movingDirection == "l":
            if grid[(x, y - 1)] == 0:
                movingDirection = "d"
                x, y = x, y - 1
            else:
                x, y = x - 1, y
        else:
            if grid[(x + 1 , y)] == 0:
                movingDirection = "r"
                x, y = x + 1, y
            else:
                x, y = x, y - 1

        toAdd = 0
        possible = [-1, 0, 1]
        combinations = itertools.product(possible, repeat=2)
        for combination in combinations:
            toAdd += grid[x + combination[0], y + combination[1]]
        grid[(x,y)] = toAdd
        current = toAdd
    return current

print(part1())
print(part2())
