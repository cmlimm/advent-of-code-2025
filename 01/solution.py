import os
import pathlib


class Dial:
    def __init__(self, max_value, starting_point) -> None:
        self.max = max_value + 1
        self.current = starting_point
        self.prev = self.current

        self.stop_at_zero_counter = 0
        self.any_zero_counter = 0

    def add(self, value) -> None:
        self.prev = self.current
        self.current = (self.current + value) % self.max
        self.calculate_counters(value)

    def subtract(self, value) -> None:
        self.prev = (self.max - self.current) % self.max
        # print(f"{self.current} -> {self.prev}")
        self.current = (self.current - value) % self.max
        self.calculate_counters(value)

    def calculate_counters(self, value) -> None:
        if self.current == 0:
            self.stop_at_zero_counter += 1

        self.any_zero_counter += (self.prev + value % self.max) // self.max + value // self.max


filepath = os.path.join(pathlib.Path(__file__).parent.absolute(), "input.in")

with open(filepath, "r") as file:
    commands_text = file.readlines()

commands = [(command[0], int(command[1:])) for command in commands_text]

filepath1 = os.path.join(pathlib.Path(__file__).parent.absolute(), "output.out")

with open(filepath1, "w") as file:
    dial = Dial(99, 50)
    zero_counter = 0
    for dir, value in commands:
        if dir == "L":
            dial.subtract(value)
        if dir == "R":
            dial.add(value)

        file.write(f"{dir}{value}: {dial.current}, {dial.any_zero_counter}\n")

    print(f"Zero Counter: {dial.stop_at_zero_counter}")
    print(f"Any Counter: {dial.any_zero_counter}")
