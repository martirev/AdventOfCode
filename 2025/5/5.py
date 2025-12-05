file = "5/test.txt"

def file_to_list(file):
    with open(file, "r") as f:
        lines = f.read().strip().splitlines()
        ranges = []
        ids = []
        empty = True
        for line in lines:
            if not line.strip():
                empty = False
                continue
            if empty:
                ranges.append(line.split("-"))
            else:
                ids.append(line)
        ids = list(map(int, ids))
        ranges = [list(map(int,x)) for x in ranges]
    return ranges, ids

def check_id(id, ranges):
    for range in ranges:
        if range[0] <= id <= range[1]:
            return True
    return False

def part1():
    ranges, ids = file_to_list(file)
    total = 0
    for id in ids:
        if check_id(id, ranges):
            total += 1
    return total

def part2():
    ranges, ids = file_to_list(file)
    new_ranges = []
    ranges.sort(key=lambda x: x[0])
    for r in ranges:
        flag = False
        for r2 in ranges:
            if r == r2:
                continue
            if r[0] <= r2[0] <= r[1]:
                new_ranges.append([r[0],r2[1]])
                flag = True
        if not flag:
            new_ranges.append([r[0],r[1]])
    return new_ranges


print(part1())
print(part2())
