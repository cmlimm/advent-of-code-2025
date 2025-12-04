import os
import pathlib


def pad_matrix(matrix, pad_size, pad_symbol=".") -> list[list[str]]:
    columns_n = len(matrix[0])
    matrix = [[pad_symbol] * columns_n] * pad_size + matrix + [[pad_symbol] * columns_n] * pad_size
    matrix = [[pad_symbol] * pad_size + row + [pad_symbol] * pad_size for row in matrix]
    return matrix


def count_neighbours(matrix, i, j, roll_symbol="@") -> int:
    modifiers = [(-1, -1), (-1, 0), (-1, +1), (0, -1), (0, +1), (+1, -1), (+1, 0), (+1, +1)]
    total = 0
    for i_mod, j_mod in modifiers:
        if matrix[i + i_mod][j + j_mod] == roll_symbol:
            total += 1
    return total


def remove_rolls(matrix, removed=0, roll_symbol="@") -> tuple[list[list[str]], int]:
    removable = []
    for i in range(1, len(matrix) - 1):
        for j in range(1, len(matrix[0]) - 1):
            if rolls[i][j] == roll_symbol and count_neighbours(matrix, i, j, roll_symbol) < 4:
                removable.append((i, j))

    if removable:
        for i, j in removable:
            matrix[i][j] = "."
        matrix, removed = remove_rolls(matrix, removed + len(removable))

    return matrix, removed


filepath = os.path.join(pathlib.Path(__file__).parent.absolute(), "input.in")

with open(filepath, "r") as file:
    rolls = [list(line.strip()) for line in file.readlines()]

rolls = pad_matrix(rolls, 1)

# Part 1

accessible_count = 0
for i in range(1, len(rolls) - 1):
    for j in range(1, len(rolls[0]) - 1):
        if rolls[i][j] == "@" and count_neighbours(rolls, i, j) < 4:
            accessible_count += 1

print(accessible_count)

# Part 2

matrix, removed = remove_rolls(rolls)
print(removed)
