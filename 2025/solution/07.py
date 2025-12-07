import sys
from collections import Counter

with open(sys.argv[1] if len(sys.argv) > 1 else "../input/07") as f:
    grid = f.read().splitlines()

beams = Counter({grid[0].index("S"): 1})
p1 = 0
for line in grid[1:]:
    new_beams = Counter()
    for beam in beams:
        if line[beam] == "^":
            new_beams[beam - 1] += beams[beam]
            new_beams[beam + 1] += beams[beam]
            p1 += 1
        else:
            new_beams[beam] += beams[beam]
    beams = new_beams

print(p1)
print(beams.total())
