import sys

with open(sys.argv[1] if len(sys.argv) > 1 else '../input/10') as f:
    tiles = f.read().splitlines()

class xy(tuple):
    def __new__(cls, x, y):
        return super(xy, cls).__new__(cls, (x, y))

    def __add__(self, other):
        return xy(*(a + b for a, b in zip(self, other)))

    def __sub__(self, other):
        return xy(*(a - b for a, b in zip(self, other)))

    def __neg__(self):
        return xy(*(-a for a in self))

loop =[]
for y, line in enumerate(tiles):
    x = line.find('S')
    if x != -1:
        loop.append(xy(x, y))
        break

north, south, east, west = xy(0,-1), xy(0,1), xy(1,0), xy(-1,0)
pipes = {
        '|': [north, south],
        '-': [east, west],
        'L': [north, east],
        'J': [north, west],
        '7': [south, west],
        'F': [south, east],
        }

tiles_xy = lambda x, y: tiles[y][x]

for d in north, south, east, west:
    loc = loop[0]+d
    if tiles_xy(*loc) in pipes and -d in pipes[tiles_xy(*loc)]:
        break

while loc != loop[0]:
    loop.append(loc)
    prev = pipes[tiles_xy(*loc)].index(loop[-2]-loc)
    loc += pipes[tiles_xy(*loc)][1-prev]

print(len(loop)//2)

pipes['S'] = [loop[1]-loop[0], loop[-1]-loop[0]]
loop_set = set(loop)
p2count = 0
for y in range(1, len(tiles)-1):
    cross_count = 0
    for x in range(len(tiles[y])-1):
        if (x, y) in loop_set:
            cross_count += north in pipes[tiles_xy(x, y)]
        else:
            p2count += cross_count%2

print(p2count)
