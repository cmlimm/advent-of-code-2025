import math
import os
import pathlib
from itertools import batched

filepath = os.path.join(pathlib.Path(__file__).parent.absolute(), "input.in")

with open(filepath, "r") as file:
    ranges_text = file.readlines()

ranges_numbers = [[int(number_text) for number_text in range_text.split("-")] for range_text in "".join(ranges_text).split(",")]

# Part 1

invalid_numbers = []
for start, finish in ranges_numbers:
    for n in range(start, finish + 1):
        digit_count = int(math.log10(n)) + 1
        if digit_count % 2 == 0:
            divisor = 10 ** (digit_count / 2)
            half1 = n // divisor
            half2 = n % divisor
            if half1 == half2:
                invalid_numbers.append(n)
print(sum(invalid_numbers))

# Part 2

invalid_numbers = []
for start, finish in ranges_numbers:
    for n in range(start, finish + 1):
        digit_count = int(math.log10(n)) + 1
        for batch_size in range(1, digit_count // 2 + 1):
            batches = batched(str(n), batch_size)
            if len(set(batches)) == 1:
                invalid_numbers.append(n)
                break
print(sum(invalid_numbers))
