file = "4/4.txt"

def file_to_list(file):
    with open(file, "r") as f:
        lines = f.read().strip().splitlines()
    return lines

def part1():
    lines = file_to_list(file)
    y_length = len(lines)
    x_length = len(lines[0])
    total = 0
    for y in range(y_length):
        for x in range(x_length):
            count = 0
            if lines[y][x] != "@":
                continue
            for i_y in range(-1,2):
                for i_x in range(-1,2):
                    check_x = x + i_x
                    check_y = y + i_y
                    if not (0 <= check_x < x_length and 0 <= check_y < y_length):
                        continue
                    if check_x == x and check_y == y:
                        continue
                    if lines[check_y][check_x] == "@":
                        count += 1
            if count < 4:
                total += 1
    return total

def part2():
    lines = file_to_list(file)
    lines = [list(x) for x in lines]
    y_length = len(lines)
    x_length = len(lines[0])
    total = 0
    delta = 1
    while delta > 0:
        delta = 0
        to_remove = []
        for y in range(y_length):
            for x in range(x_length):
                count = 0
                if lines[y][x] != "@":
                    continue
                for i_y in range(-1,2):
                    for i_x in range(-1,2):
                        check_x = x + i_x
                        check_y = y + i_y
                        if not (0 <= check_x < x_length and 0 <= check_y < y_length):
                            continue
                        if check_x == x and check_y == y:
                            continue
                        if lines[check_y][check_x] == "@":
                            count += 1
                if count < 4:
                    delta += 1
                    to_remove.append([y,x])
        total += delta
        for par in to_remove:
            lines[par[0]][par[1]] = "."
    return total

print(part1())
print(part2())
