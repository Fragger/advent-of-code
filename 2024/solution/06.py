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
visited = {start}
while 0 < loc[0] < xlen-1 and 0 < loc[1] < ylen-1:
    x, y = loc[0]+dirs[orent][0], loc[1]+dirs[orent][1]
    if labmap[y][x] == '#':
        orent = (orent+1)%4
    else:
        loc = x, y
        visited.add(loc)
print(len(visited))

def loop(block):
    orent = 0
    loc = start
    visited = {start+(orent,)}
    while 0 < loc[0] < xlen-1 and 0 < loc[1] < ylen-1:
        x, y = loc[0]+dirs[orent][0], loc[1]+dirs[orent][1]
        if labmap[y][x] == '#' or (x, y) == block:
            orent = (orent+1)%4
        else:
            loc = x, y
            visit = x, y, orent
            if visit in visited:
                return True
            visited.add(visit)
    return False
print(sum(map(loop, visited)))
