file = "3/3.txt"

def file_to_list(file):
    with open(file, "r") as f:
        lines = f.read().strip().splitlines()
        numbers = [list(map(int,line)) for line in lines]
    return numbers

def part1():
    numbers = file_to_list(file)
    total = 0
    for line in numbers:
        best = 0
        secound_best = 0
        length = len(line)
        for indeks, number in enumerate(line): 
            if number > best and indeks != (length-1):
                secound_best = 0
                best = number
                continue
            if number > secound_best:
                secound_best = number
        total += best * 10 + secound_best
    return total

def part2():
    numbers = file_to_list(file)
    total = 0
    for line in numbers:
        count = 12
        best_numbers = [0]*count
        length = len(line)
        for indeks, number in enumerate(line): 
            for i in range(0,count):
                away_from_last = (length + 1- (count-i ))
                if number > best_numbers[i] and indeks < away_from_last:
                    best_numbers[i] = number
                    best_numbers = best_numbers[:i+1] + [0]*len(best_numbers[i+1:])
                    break
        str_numbers = [str(x) for x in best_numbers]
        total += int("".join(str_numbers))
    return total

print(part1())
print(part2())
