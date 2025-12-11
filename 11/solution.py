import os
import pathlib
from functools import cache

filepath = os.path.join(pathlib.Path(__file__).parent.absolute(), "input.in")

with open(filepath, "r") as file:
    input = [line.split(" ") for line in file.readlines()]

server_rack = {line[0][:-1]: [item.strip() for item in line[1:]] for line in input}
# print(server_rack)


def dfs_with_count(start, end, graph, count, visited=set()) -> None:
    if start == end:
        count[0] += 1
        return

    visited.add(start)
    for i in graph[start]:
        if not i in visited:
            dfs_with_count(i, end, graph, count, visited)

    visited.remove(start)


@cache
def dfs_cachable(start, end) -> int:
    if start == end:
        return 1
    if end == "fft" and start == "out":
        return 0
    if end == "dac" and start == "out":
        return 0

    count = 0
    for i in server_rack[start]:
        count += dfs_cachable(i, end)

    return count


# Part 1

count = [0]
dfs_with_count("you", "out", server_rack, count, set())
print(count)

# Part 2

svr_to_fft = dfs_cachable("svr", "fft")
print("svr_to_fft: ", svr_to_fft)

fft_to_dac = dfs_cachable("fft", "dac")
print("fft_to_dac: ", fft_to_dac)

dac_to_out = dfs_cachable("dac", "out")
print("dac_to_out: ", dac_to_out)

total = svr_to_fft * fft_to_dac * dac_to_out
print(total)
