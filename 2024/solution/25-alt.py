import sys
from itertools import combinations

with open(sys.argv[1] if len(sys.argv) > 1 else '../input/25') as f:
    schematics = [{(x, y) for y, line in enumerate(sch.splitlines()) for x, c in enumerate(line) if c == '#'}
                  for sch in f.read().split('\n\n')]

print(sum(a.isdisjoint(b) for a, b in combinations(schematics, 2)))
