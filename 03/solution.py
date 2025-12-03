import os
import pathlib

filepath = os.path.join(pathlib.Path(__file__).parent.absolute(), "input.in")

with open(filepath, "r") as file:
    banks_text = file.readlines()

banks = [list(map(int, bank_text.strip())) for bank_text in banks_text]

# Part 1

joltages = []
for bank in banks:
    first = -1
    second = -1
    bank_length = len(bank)
    for idx, battery in enumerate(bank):
        if battery > first and idx != bank_length - 1:
            first = battery
            second = -1
            continue
        if battery > second:
            second = battery
    joltages.append(first * 10 + second)

print(sum(joltages))

# Part 2

joltages = []
for bank in banks:
    selected_batteries = [-1] * 12
    bank_length = len(bank)
    for idx, battery in enumerate(bank):
        for digit_n in range(12):
            if battery > selected_batteries[digit_n] and idx < (bank_length - 12) + (digit_n + 1):
                selected_batteries[digit_n] = battery
                if digit_n + 1 < len(bank):
                    selected_batteries[digit_n + 1 :] = [-1] * (12 - digit_n)
                break
    joltages.append(sum([digit * 10 ** (12 - power - 1) for digit, power in zip(selected_batteries, range(12))]))

print(sum(joltages))
