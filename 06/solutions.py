import os
import pathlib
import re
from functools import reduce
from itertools import groupby

filepath = os.path.join(pathlib.Path(__file__).parent.absolute(), "input.in")

# Part 1

with open(filepath, "r") as file:
    input = [re.split(" +", line.strip()) for line in file.readlines()]

operands_lists_str, operators = input[:-1], input[-1]
operands_lists = [[int(operand) for operand in operand_list] for operand_list in operands_lists_str]
operations_n = len(operators)

total = 0
for idx in range(operations_n):
    operands = [operand_list[idx] for operand_list in operands_lists]
    operator = operators[idx]

    result = 0
    if operator == "+":
        result = reduce(lambda x, y: x + y, operands, 0)
    elif operator == "*":
        result = reduce(lambda x, y: x * y, operands, 1)
    total += result

print(total)

# Part 2

with open(filepath, "r") as file:
    input2 = [list(line.strip("\n")) for line in file.readlines()]

transposed_input = zip(*input2)
joined_transposed_input = ["".join(line) for line in transposed_input]
groups = groupby(joined_transposed_input, lambda x: re.fullmatch(" +", x))

total = 0
for is_spaces, group in groups:
    if not is_spaces:
        operation = list(group)
        operator = operation[0][-1]
        operation[0] = operation[0][:-1]
        operands = [int(item.strip()) for item in operation]

        result = 0
        if operator == "+":
            result = reduce(lambda x, y: x + y, operands, 0)
        elif operator == "*":
            result = reduce(lambda x, y: x * y, operands, 1)
        total += result

print(total)
