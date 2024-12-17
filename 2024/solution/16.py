import sys
import heapq
from collections import deque

with open(sys.argv[1] if len(sys.argv) > 1 else '../input/16') as f:
    maze = {(x, y): c for y, line in enumerate(f.read().splitlines()) for x, c in enumerate(line)}

start = next(pos for pos, c in maze.items() if c == 'S')
end = next(pos for pos, c in maze.items() if c == 'E')

def moves(node):
    score, (x, y), (dx, dy) = node
    nxy = x+dx, y+dy
    if maze[nxy] != '#':
        yield score+1, (nxy, (dx, dy))
    for ndx, ndy in (dy, dx), (-dy, -dx):
        yield score+1000, ((x, y), (ndx, ndy))

nodes = [(0, start, (1, 0))]
seen = {}
while (node:=heapq.heappop(nodes))[1] != end:
    for score, cur in moves(node):
        if cur not in seen:
            heapq.heappush(nodes, (score,)+cur)
            seen[cur] = [score, {node[1:3]}]
        elif score == seen[cur][0]:
            seen[cur][1].add(node[1:3])
print(node[0])

path = set()
queue = deque([node[1:3]])
while queue:
    cur = queue.pop()
    path.add(cur[0])
    if cur[0] != start:
        for parent in seen[cur][1]:
            queue.append(parent)
print(len(path))
