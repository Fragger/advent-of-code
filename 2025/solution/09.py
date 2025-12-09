import sys
from itertools import chain, combinations, pairwise

with open(sys.argv[1] if len(sys.argv) > 1 else "../input/09") as f:
    red_tiles = [tuple(map(int, line.split(","))) for line in f]

rects = []
for a, b in combinations(red_tiles, 2):
    x1, x2 = sorted((a[0], b[0]))
    y1, y2 = sorted((a[1], b[1]))
    rects.append(((x2 - x1 + 1) * (y2 - y1 + 1), x1, y1, x2, y2))
rects.sort(reverse=True)

print(rects[0][0])

perimeter = []
for a, b in pairwise(chain(red_tiles, red_tiles[:1])):
    x1, x2 = sorted((a[0], b[0]))
    y1, y2 = sorted((a[1], b[1]))
    perimeter.append((x1, y1, x2, y2))

for area, rx1, ry1, rx2, ry2 in rects:
    for lx1, ly1, lx2, ly2 in perimeter:
        if rx1 < lx2 and rx2 > lx1 and ry1 < ly2 and ry2 > ly1:
            break
    else:
        print(area)
        break
