import bisect
import os
import pathlib
from functools import reduce
from math import sqrt

from tqdm import tqdm


def distance(point1, point2) -> float:
    return sqrt(sum([(c1 - c2) ** 2 for c1, c2 in zip(point1, point2)]))


filepath = os.path.join(pathlib.Path(__file__).parent.absolute(), "input.in")

with open(filepath, "r") as file:
    points = [list(map(int, line.split(","))) for line in file.readlines()]

n_points = len(points)

distances: list[tuple[set[int], float]] = []
for i in tqdm(range(n_points - 1)):
    for j in range(i + 1, n_points):
        dist = distance(points[i], points[j])
        bisect.insort(distances, ({i, j}, dist), key=lambda x: x[-1])

max_connections_count = 1000
connections = [distance[0] for distance in distances]

groups_part1: list[set[int]] = []
groups: list[set[int]] = []
final_connection: list[int]

for idx, connection in enumerate(tqdm(connections)):
    non_intesecting = []
    intersecting = set(connection)

    for group in groups:
        if connection.intersection(group):
            intersecting |= set(group)
        else:
            non_intesecting.append(set(group))

    groups = non_intesecting + [intersecting]

    # Calculations for Part 1 stop here
    if idx + 1 == max_connections_count:
        groups_part1 = groups

    # Calculations for Part 2 stop here
    if len(groups) == 1 and len(groups[0]) == n_points:
        final_connection = list(connection)
        break

# Part 1

groups_lengths = [len(group) for group in groups_part1]
groups_lengths.sort()
print(reduce(lambda x, y: x * y, groups_lengths[-3:], 1))

# Part 2

print(points[final_connection[0]][0] * points[final_connection[1]][0])
