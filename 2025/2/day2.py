file = "2/day2.txt"

def file_to_list(file):
    with open(file, "r") as f:
        ranges = f.read().strip().split(",")
    return ranges

def part1():
    ranges = file_to_list(file)
    total = 0
    for r in ranges:
        start, stop = r.split("-")
        for i in range(int(start),int(stop) + 1):
            number_string = str(i)
            if len(number_string) % 2 == 0:
                length = len(number_string)//2
                first_block = number_string[:length]
                second_block = number_string[length:]
                if first_block == second_block:
                    total += i 
    return total

def factors(n):
    factorss = []
    for i in range(1, n):
        if n % i == 0:
            factorss.append(i)
    return factorss

def part2():
    ranges = file_to_list(file)
    total = 0
    for r in ranges:
        start, stop = r.split("-")
        for i in range(int(start),int(stop) + 1):
            number_string = str(i)
            t_factors = factors(int(len(str(i))))
            for sub_string_length in t_factors:
                sub_strings = []
                sub_string_count = len(number_string)//sub_string_length
                for j in range(sub_string_count):
                    sub_strings.append(number_string[j * sub_string_length: (j+1)*sub_string_length])
                if len(set(sub_strings)) == 1:
                    total += i
                    break
    return total


print(part1())
print(part2())
