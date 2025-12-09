import os
import pathlib
from itertools import combinations

from tqdm import tqdm


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

# Part 2

# import numpy as np
# from skimage.draw import line
# from skimage.io import imsave

# img = np.ones((1000, 1000), dtype=np.uint8)
# for idx, (y, x) in enumerate(coordinates[:-1]):
#     b, a = coordinates[idx + 1]
#     rr, cc = line(int(x / 100), int(y / 100), int(a / 100), int(b / 100))
#     img[rr, cc] = 0

# rr, cc = line(
#     int(coordinates[-1][1] / 100), int(coordinates[-1][0] / 100), int(coordinates[0][1] / 100), int(coordinates[0][0] / 100)
# )
# img[rr, cc] = 0
# filepath = os.path.join(pathlib.Path(__file__).parent.absolute(), "img.tif")
# imsave(filepath, img)

max_area = 0
max_area_coords = []
for c1, c2 in tqdm(combinations(coordinates, 2)):
    valid = True
    min_y, max_y = sorted([c1[0], c2[0]])
    min_x, max_x = sorted([c1[1], c2[1]])

    for idx, coord in enumerate(coordinates[:-1]):
        next_coord = coordinates[idx + 1]
        line_min_y, line_max_y = sorted([coord[0], next_coord[0]])
        line_min_x, line_max_x = sorted([coord[1], next_coord[1]])
        # если линия _полностью_ внутри прямоугольника, то внутри окажется белый пиксель
        if min_y < line_max_y and max_y > line_min_y and min_x < line_max_x and max_x > line_min_x:
            valid = False
            break
        # + отсекаем горизонтальные линии посередине
        if min_x > line_min_x and max_x < line_max_x:
            valid = False
            break

    coord = coordinates[-1]
    next_coord = coordinates[0]
    line_min_y, line_max_y = sorted([coord[0], next_coord[0]])
    line_min_x, line_max_x = sorted([coord[1], next_coord[1]])
    if min_y < line_max_y and max_y > line_min_y and min_x < line_max_x and max_x > line_min_x:
        valid = False

    if valid:
        area = get_area(c1, c2)
        if area >= max_area:
            max_area = area
            max_area_coords = [c1, c2]

print(max_area)
