import sys
from collections import defaultdict
from itertools import permutations

with open(sys.argv[1] if len(sys.argv) > 1 else '../input/08') as f:
    antmap = f.read().splitlines()

xlen = len(antmap[0])
ylen = len(antmap)

ants = defaultdict(list)
for y in range(ylen):
    for x in range(xlen):
        if antmap[y][x] != '.':
            ants[antmap[y][x]].append((x, y))

p1 = set()
p2 = set()
for ant in ants.values():
    for (ax, ay), (bx, by) in permutations(ant, 2):
        dx, dy = bx-ax, by-ay
        i = 0
        while 0 <= (nx:=ax-dx*i) < xlen and 0 <= (ny:=ay-dy*i) < ylen:
            if i == 1:
                p1.add((nx, ny))
            p2.add((nx, ny))
            i += 1
        i = 1
        while 0 <= (nx:=bx+dx*i) < xlen and 0 <= (ny:=by+dy*i) < ylen:
            if i == 1:
                p1.add((nx, ny))
            p2.add((nx, ny))
            i += 1
print(len(p1))
print(len(p2))
