import os
import pathlib


def buttons_to_increases(list_buttons, max_n) -> list[int]:
    initial = [0] * max_n
    for button in list_buttons:
        initial[button] = 1
    return initial


def indicators_to_set(list_str) -> set[int]:
    return {idx for idx, symbol in enumerate(list_str) if symbol == "#"}


filepath = os.path.join(pathlib.Path(__file__).parent.absolute(), "input.in")

with open(filepath, "r") as file:
    diagram = [line.split(" ") for line in file.readlines()]

machines = [
    (
        indicators_to_set(list(line[0].strip("[]"))),
        [set(map(int, item.strip("()").split(","))) for item in line[1:-1]],
        list(map(int, line[-1].strip("\n{}").split(","))),
    )
    for line in diagram
]

# Part 1

paths = []
for machine in machines:
    print()
    print(machine)

    target = machine[0]
    moves = machine[1]

    visited = set()
    queue = []

    queue.append((set(), 0))
    visited.add(frozenset())

    while queue:
        current, path = queue.pop(0)
        if current == target:
            print(current, path)
            paths.append(path)
            break

        neighbours = [current ^ move for move in moves]
        for neighbour in neighbours:
            if not neighbour in visited:
                queue.append((neighbour, path + 1))
                visited.add(frozenset(neighbour))

print(sum(paths))

# Part 2

from scipy.optimize import linprog

press_count = 0
for machine in machines:
    target_vector = machine[-1]
    lights_count = len(machine[-1])
    buttons = machine[1]
    increases = [buttons_to_increases(button, lights_count) for button in buttons]

    c = [1] * len(buttons)
    a_eq = list(map(list, zip(*increases)))
    b_eq = target_vector

    result = linprog(c, A_eq=a_eq, b_eq=b_eq, integrality=1)
    press_count += sum(result.x)

print(int(press_count))
