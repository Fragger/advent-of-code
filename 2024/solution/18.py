import sys
from collections import deque

with open(sys.argv[1] if len(sys.argv) > 1 else '../input/18') as f:
    cords = [tuple(map(int, line.split(','))) for line in f.read().splitlines()]

space = 70
i = 1024

corrupted = set(cords[:i])

while i < len(cords):
    seen = {}
    queue = deque([(0, (0, 0))])
    while queue:
        steps, (x, y) = queue.popleft()
        if (x, y) == (space, space):
            if i == 1024:
                print(steps)
            break
        for dx, dy in (0, -1), (1, 0), (0, 1), (-1, 0):
            nx, ny = x+dx, y+dy
            if (0 <= nx <= space and 0 <= ny <= space and
                (nx, ny) not in corrupted and (nx, ny) not in seen):
                seen[nx, ny] = x, y
                queue.append((steps+1, (nx, ny)))
    else:
        print(','.join(map(str, cords[i-1])))
        break

    path = set()
    loc = (space, space)
    while loc != (0, 0):
        path.add(loc)
        loc = seen[loc]

    while cords[i-1] not in path:
        corrupted.add(cords[i])
        i += 1
