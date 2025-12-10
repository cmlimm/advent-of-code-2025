import os
import pathlib

from tqdm import tqdm


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

        neighbours = [(current ^ move, move) for move in moves]
        for neighbour, move in neighbours:
            if not neighbour in visited:
                queue.append((neighbour, path + 1))
                visited.add(frozenset(neighbour))

print(sum(paths))

# Part 2

# paths = []
# for machine in machines:
#     print()
#     print(machine)

#     target_joltsages = machine[-1]
#     max_n = len(target_joltsages)
#     moves_j = [buttons_to_increases(buttons, max_n) for buttons in machine[1]]

#     visited_j = set()
#     queue_j = []
#     initial_j = [0] * max_n
#     queue_j.append((initial_j, 0))
#     visited_j.add(tuple(initial_j))

#     while queue_j:
#         current_j, path_j = queue_j.pop(0)
#         if current_j == target_joltsages:
#             print(current_j, path_j)
#             paths.append(path_j)
#             break

#         neighbours_j = [([i + j for i, j in zip(current_j, move)], move) for move in moves_j]
#         for neighbour, move in neighbours_j:
#             t_neighbour = tuple(neighbour)
#             if not t_neighbour in visited_j:
#                 queue_j.append((neighbour, path_j + 1))
#                 visited_j.add(t_neighbour)

# print(sum(paths))
