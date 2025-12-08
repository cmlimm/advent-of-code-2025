import os
import pathlib
from collections import Counter

filepath = os.path.join(pathlib.Path(__file__).parent.absolute(), "input.in")

with open(filepath, "r") as file:
    diagram = [list(line.strip()) for line in file.readlines()[::2]]


# Part 1
# can be calculated at the same time with the Part 2, but left for history

beam_positions = {diagram[0].index("S")}
split_count = 0

for row in diagram:
    splitter_positions = [i for i, x in enumerate(row) if x == "^"]
    pos_to_remove = set()
    pos_to_add = set()
    for beam_position in beam_positions:
        if beam_position in splitter_positions:
            split_count += 1
            pos_to_remove.add(beam_position)
            pos_to_add |= {beam_position - 1, beam_position + 1}

    beam_positions -= pos_to_remove
    beam_positions |= pos_to_add

print(split_count)

# Part 2

beam_positions2 = Counter({diagram[0].index("S"): 1})

for row in diagram:
    splitter_positions = [i for i, x in enumerate(row) if x == "^"]

    pos_to_remove2 = []
    pos_to_add2 = Counter()
    for beam_position, path_count in beam_positions2.items():
        if beam_position in splitter_positions:
            pos_to_remove2.append(beam_position)
            pos_to_add2.update(Counter({beam_position - 1: path_count, beam_position + 1: path_count}))

    for pos in pos_to_remove2:
        del beam_positions2[pos]
    beam_positions2.update(pos_to_add2)

print(beam_positions2.total())
