from collections import defaultdict


input = "3935565 31753 437818 7697 5 38 0 123"
test_input = "125 17"


def part12(n):
    blinks = n
    numbers = defaultdict(lambda: 0)
    for number in input.split():
        numbers[int(number)] = 1
    for _ in range(blinks):
        numbers = dict_blink(numbers)
    return sum([x for x in numbers.values()])


def dict_blink(numbers: dict):
    blinked_dict = defaultdict(lambda: 0)
    for key, value in numbers.items():
        length = len(str(key))
        if key == 0:
            blinked_dict[1] += value
        elif length % 2 == 0:
            blinked_dict[int(str(key)[: length // 2])] += value
            blinked_dict[int(str(key)[length // 2 :])] += value
        else:
            blinked_dict[key * 2024] += value
    return blinked_dict


print(part12(25))
print(part12(75))
