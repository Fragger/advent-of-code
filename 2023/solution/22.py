import sys
from operator import itemgetter
from collections import namedtuple

with open(sys.argv[1] if len(sys.argv) > 1 else '../input/22') as f:
    rawbricks = [tuple(int(n)
            for xyz in line.strip().split('~') for n in xyz.split(','))
            for line in f]

rawbricks.sort(key=itemgetter(2))

Bricks = namedtuple('Bricks', ('above', 'below'))
bricks = {}
for x1, y1, z1, x2, y2, z2 in rawbricks:
    zd = z2-z1

    z1 = 1 + max((cz2
        for cx1, cy1, cz1, cx2, cy2, cz2 in bricks
        if x1 <= cx2 and x2 >= cx1 and y1 <= cy2 and y2 >= cy1),
        default=0)

    z2 = z1 + zd

    below = set()
    for cx1, cy1, cz1, cx2, cy2, cz2 in bricks:
        if cz2 + 1 == z1 and x1 <= cx2 and x2 >= cx1 and y1 <= cy2 and y2 >= cy1:
            bricks[cx1, cy1, cz1, cx2, cy2, cz2].above.add((x1, y1, z1, x2, y2, z2))
            below.add((cx1, cy1, cz1, cx2, cy2, cz2))

    bricks[x1, y1, z1, x2, y2, z2] = Bricks(set(), below)

print(sum(
    all(len(bricks[brick][1]) > 1 for brick in holding)
    for holding, _ in bricks.values()))

p2 = 0
for nextbrick in bricks:
    fall = [nextbrick]
    fallset = set(fall)
    for testbrick in fall:
        for brick in bricks[testbrick].above:
            below = bricks[brick].below
            if below and below <= fallset and brick not in fallset:
                fall.append(brick)
                fallset.add(brick)

    p2 += len(fallset) - 1

print(p2)
