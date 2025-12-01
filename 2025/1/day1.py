file = "1/day1.txt"

def file_to_list(file):
    with open(file, "r") as f:
        lines = f.read().strip().splitlines()
        movements = []
        for line in lines:
            lr, n = line[0],line[1:]
            movements.append([lr,n])
    return movements


def part1():
    movements = file_to_list(file)
    current_indx = 50
    n = 0
    for move in movements:
        lr = move[0]
        distance = int(move[1])
        if move[0] == "L":
            current_indx = (current_indx - distance) % 100
        else:
            current_indx = (current_indx + distance) % 100
        if current_indx == 0:
            n += 1
    return n


def part2():
    movements = file_to_list(file)
    current_indx = 50
    min_indx, max_indx = 0,99
    n = 0
    for move in movements:
        lr = move[0]
        distance = int(move[1])
        for _ in range(distance):
            if lr == "L":
                current_indx -= 1
                if current_indx == 0:
                    n += 1
                if current_indx == min_indx - 1:
                    current_indx = max_indx
            else:
                current_indx += 1
                if current_indx == max_indx + 1:
                    current_indx = min_indx
                    n += 1
    return n


print(part1())
print(part2())
