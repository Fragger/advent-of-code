import sys

with open(sys.argv[1] if len(sys.argv) > 1 else '../input/06') as f:
    labmap = f.read().splitlines()

xlen = len(labmap[0])
ylen = len(labmap)

for y in range(ylen):
    for x in range(xlen):
        if labmap[y][x] == '^':
            loc = x, y

dirs = ((0, -1), (1, 0), (0, 1), (-1, 0))

orent = 0
start = loc
visited1 = {start}
while 0 < loc[0] < xlen-1 and 0 < loc[1] < ylen-1:
    x, y = loc[0]+dirs[orent][0], loc[1]+dirs[orent][1]
    if labmap[y][x] == '#':
        orent = (orent+1)%4
    else:
        loc = x, y
        visited1.add(loc)
print(len(visited1))

p2 = 0
for block in visited1:
    orent = 0
    loc = start
    visited2 = {start+(orent,)}
    while 0 < loc[0] < xlen-1 and 0 < loc[1] < ylen-1:
        x, y = loc[0]+dirs[orent][0], loc[1]+dirs[orent][1]
        if labmap[y][x] == '#' or (x, y) == block:
            orent = (orent+1)%4
        else:
            loc = x, y
            visit = x, y, orent
            if visit in visited2:
                p2 += 1
                break
            visited2.add(visit)
print(p2)
