import os
import pathlib

filepath = os.path.join(pathlib.Path(__file__).parent.absolute(), "input.in")

with open(filepath, "r") as file:
    database = [line.strip() for line in file.readlines()]

empty_string_idx = database.index("")
fresh_ranges = [tuple(map(int, fresh_range.split("-"))) for fresh_range in database[:empty_string_idx]]
ingredients = [int(ingredient) for ingredient in database[empty_string_idx + 1 :]]

# Part 1

total_fresh = 0
for ingredient in ingredients:
    for start, end in fresh_ranges:
        if start <= ingredient <= end:
            total_fresh += 1
            break

print(total_fresh)

# Part 2

fresh_ranges.sort(key=lambda x: x[0])
joined_ranges = [fresh_ranges[0]]

for start, end in fresh_ranges[1:]:
    start_last, end_last = joined_ranges[-1]

    if start <= end_last:
        joined_ranges[-1] = (min(start, start_last), max(end, end_last))
    else:
        joined_ranges.append((start, end))

total_fresh = 0
for start, end in joined_ranges:
    total_fresh += end - start + 1
print(total_fresh)
