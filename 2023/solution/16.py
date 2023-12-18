import sys
from collections import deque

with open(sys.argv[1] if len(sys.argv) > 1 else '../input/16') as f:
    tiles = f.read().splitlines()

up, down, left, right = (0 ,-1), (0, 1), (-1, 0), (1, 0)
items = {'.': {right: [right],
              left: [left],
              down: [down],
              up: [up]},
        '/': {right: [up],
              left: [down],
              down: [left],
              up: [right]},
        '\\': {right: [down],
              left: [up],
              down: [right],
              up: [left]},
        '|': {right: [up, down],
              left: [up, down],
              down: [down],
              up: [up]},
        '-': {right: [right],
              left: [left],
              down: [right, left],
              up: [right, left]},
        }

tiles_xy = lambda x, y: tiles[y][x]

xlen = len(tiles[0])
ylen = len(tiles)
def energized(s_loc, s_heading):
    seen = set()
    queue = deque()
    seen.add((s_loc, s_heading))
    queue.append((s_loc, s_heading))
    while queue:
        loc, heading = queue.popleft()
        for direction in items[tiles_xy(*loc)][heading]:
            next_loc = loc[0] + direction[0], loc[1] + direction[1]
            next_lh = (next_loc, direction)
            if next_lh not in seen and 0<=next_loc[0]<xlen and 0<=next_loc[1]<ylen:
                seen.add(next_lh)
                queue.append(next_lh)
    return len(set(loc for loc, _ in seen))

print(energized((0, 0), right))

p2max = 0
for x in range(xlen):
    p2max = max(p2max, energized((x, 0), down))
    p2max = max(p2max, energized((x, ylen - 1), up))
for y in range(ylen):
    p2max = max(p2max, energized((0, y), right))
    p2max = max(p2max, energized((xlen - 1, y), left))
print(p2max)
