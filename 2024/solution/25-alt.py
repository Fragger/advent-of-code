import sys
from itertools import combinations

schematics = []
with open(sys.argv[1] if len(sys.argv) > 1 else '../input/25') as f:
    for sch in f.read().split('\n\n'):
        sch = list(sch.splitlines())
        schematics.append({(x, y) for y in range(len(sch)) for x in range(len(sch[0])) if sch[y][x] == '#'})

print(sum(a.isdisjoint(b) for a, b in combinations(schematics, 2)))
