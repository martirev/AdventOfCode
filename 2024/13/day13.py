from functools import partial
from itertools import batched
import re
import numpy as np

input = "2024/13/13.txt"


def get_input(file):
    with open(file, "r") as f:
        return f.read().strip().split("\n\n")


def part1():
    games = get_input(input)
    total_tokens = 0
    for game in games:
        XY_a, XY_b, XY_goal = batched(map(int, re.findall(r"-?\d+", game)), 2)
        a = np.array([[XY_a[0], XY_b[0]], [XY_a[1], XY_b[1]]])
        b = np.array([XY_goal[0], XY_goal[1]])
        solution = np.linalg.solve(a, b)
        a_button, b_button = map(partial(round, ndigits=7), solution)
        if (a_button).is_integer() and (b_button).is_integer():
            total_tokens += a_button * 3 + b_button
    return total_tokens


def part2():
    games = get_input(input)
    total_tokens = 0
    for game in games:
        XY_a, XY_b, XY_goal = batched(map(int, re.findall(r"-?\d+", game)), 2)
        XY_goal = [x + 10000000000000 for x in XY_goal]
        a = np.array([[XY_a[0], XY_b[0]], [XY_a[1], XY_b[1]]])
        b = np.array([XY_goal[0], XY_goal[1]])
        solution = np.linalg.solve(a, b)
        a_button, b_button = solution
        if (
            abs(a_button - round(a_button)) < 0.01
            and abs(b_button - round(b_button)) < 0.01
        ):
            total_tokens += round(a_button) * 3 + round(b_button)
    return total_tokens


print(part1())
print(part2())
