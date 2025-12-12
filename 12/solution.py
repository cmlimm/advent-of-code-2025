import os
import pathlib

filepath = os.path.join(pathlib.Path(__file__).parent.absolute(), "input.in")

with open(filepath, "r") as file:
    input = [sector.split("\n") for sector in file.read().split("\n\n")]

presents = [[[0 if symbol == "." else 1 for symbol in line] for line in list(present[1:])] for present in input[:-1]]
presents_with_count = [(sum([row.count(1) for row in present]), present) for present in presents]

regions_temp = [region.split(" ") for region in input[6]]
regions = [(tuple(map(int, region[0][:-1].split("x"))), list(map(int, region[1:]))) for region in regions_temp]
regions_with_count = [(region[0], region[0][0] * region[0][1], region[-1]) for region in regions]

# print(presents_with_count)
# print(regions_with_count)

fits_min = 0
for dimensions, free_places, counts in regions_with_count:
    taken_places = 0
    for idx, count in enumerate(counts):
        taken_places += presents_with_count[idx][0] * count
    if taken_places <= free_places:
        fits_min += 1

print(fits_min)
