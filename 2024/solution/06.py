import sys

with open(sys.argv[1] if len(sys.argv) > 1 else '../input/06') as f:
    labmap = f.read().splitlines()

xlen = len(labmap[0])
ylen = len(labmap)

for y in range(ylen):
    for x in range(xlen):
        if labmap[y][x] == '^':
            start = x, y

dirs = ((0, -1), (1, 0), (0, 1), (-1, 0))

orent = 0
x, y = start
visited = {start}
while 0 < x < xlen-1 and 0 < y < ylen-1:
    nx, ny = x+dirs[orent][0], y+dirs[orent][1]
    if labmap[ny][nx] == '#':
        orent = (orent+1)%4
    else:
        x, y = nx, ny
        visited.add((x, y))
print(len(visited))

def loop(block):
    orent = 0
    x, y = start
    visited = {(x, y, orent)}
    while 0 < x < xlen-1 and 0 < y < ylen-1:
        nx, ny = x+dirs[orent][0], y+dirs[orent][1]
        if labmap[ny][nx] == '#' or (nx, ny) == block:
            orent = (orent+1)%4
        else:
            x, y = nx, ny
            visit = x, y, orent
            if visit in visited:
                return True
            visited.add(visit)
    return False
print(sum(map(loop, visited)))
