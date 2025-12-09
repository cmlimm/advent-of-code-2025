import os
import pathlib
from itertools import combinations


def get_area(p1, p2) -> int:
    return (abs(p1[0] - p2[0]) + 1) * (abs(p1[1] - p2[1]) + 1)


filepath = os.path.join(pathlib.Path(__file__).parent.absolute(), "input.in")

with open(filepath, "r") as file:
    coordinates = [list(map(int, line.split(","))) for line in file.readlines()]

# Part 1

max_area_coords = []
max_area = -1
for c1, c2 in combinations(coordinates, 2):
    area = get_area(c1, c2)
    if area >= max_area:
        max_area = area
        max_area_coords = [c1, c2]

print(max_area)
print(max_area_coords)
