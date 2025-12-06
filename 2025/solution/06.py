import sys
from functools import reduce
from operator import add, mul

opr = {"+": add, "*": mul}

with open(sys.argv[1] if len(sys.argv) > 1 else "../input/06") as f:
    grid = f.read().splitlines()

p1_prob = [[num for num in line.split()] for line in grid]
ylen = len(p1_prob) - 1
xlen = len(p1_prob[0])

p1 = sum(
    reduce(opr[p1_prob[-1][x]], (int(p1_prob[y][x]) for y in range(ylen)))
    for x in range(xlen)
)

ylen = len(grid)
xlen = len(grid[0])

p2_prob = [
    group.splitlines()
    for group in "\n".join(
        "".join(grid[y][x] for y in range(ylen)).lstrip() for x in range(xlen)
    ).split("\n\n")
]

p2 = sum(
    reduce(opr[group[0][-1]], (int(group[y][:-1]) for y in range(len(group))))
    for group in p2_prob
)

print(p1)
print(p2)
