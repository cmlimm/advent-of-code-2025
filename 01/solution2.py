import os
import pathlib


class Dial:
    def __init__(self, max_value, starting_value) -> None:
        self.dial = list(range(max_value + 1))

        for _ in range(starting_value):
            self.rotate("R")

    def rotate(self, dir) -> None:
        if dir == "R":
            self.dial = self.dial[1:] + [self.dial[0]]
        if dir == "L":
            self.dial = [self.dial[-1]] + self.dial[:-1]

    def get_current(self) -> int:
        return self.dial[0]


filepath = os.path.join(pathlib.Path(__file__).parent.absolute(), "input.in")
with open(filepath, "r") as file:
    commands_text = file.readlines()
commands = [(command[0], int(command[1:])) for command in commands_text]

dial = Dial(99, 50)

stop_at_zero_counter = 0
any_zero_counter = 0
for dir, count in commands:
    for _ in range(count):
        dial.rotate(dir)
        if dial.get_current() == 0:
            any_zero_counter += 1
    if dial.get_current() == 0:
        stop_at_zero_counter += 1

print(f"Stop at Zero Counter: {stop_at_zero_counter}")
print(f"Any Zero Counter: {any_zero_counter}")
