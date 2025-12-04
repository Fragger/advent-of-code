import sys
from itertools import product

with open(sys.argv[1] if len(sys.argv) > 1 else "../input/04") as f:
    grid = {
        (x, y)
        for y, line in enumerate(f.read().splitlines())
        for x, char in enumerate(line)
        if char == "@"
    }

p1 = 0
p2 = 0
remove = set()
while remove or not p1:
    remove = set()
    for x, y in grid:
        if sum((x + i, y + j) in grid for i, j in product((-1, 0, 1), repeat=2)) <= 4:
            remove.add((x, y))
    if not p1:
        p1 = len(remove)
    p2 += len(remove)
    grid -= remove

print(p1)
print(p2)
