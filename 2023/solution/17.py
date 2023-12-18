import sys
import heapq

up, down, left, right = (0, -1), (0, 1), (-1, 0), (1, 0)
turn = {up: (left, right),
        down: (left, right),
        left: (up, down),
        right: (up, down),
        (0, 0): (right, down)}

with open(sys.argv[1] if len(sys.argv) > 1 else '../input/17') as f:
    blocks = [[int(block) for block in row.strip()] for row in f]

xlen = len(blocks[0])
ylen = len(blocks)

def getminheatloss(minlen, maxlen):
    nodes = [(0, (0, 0), (0, 0))]
    visited = set()
    while (node:=heapq.heappop(nodes))[1] != (xlen-1, ylen-1):
        heatloss, loc, lastdir = node
        if (loc, lastdir) in visited:
            continue
        visited.add((loc, lastdir))
        for direction in turn[lastdir]:
            newheatloss = heatloss
            for dirlen in range(1, maxlen + 1):
                newloc = loc[0] + direction[0]*dirlen, loc[1] + direction[1]*dirlen
                if not (0 <= newloc[0] < xlen and 0 <= newloc[1] < ylen):
                    break
                newheatloss += blocks[newloc[1]][newloc[0]]
                if dirlen < minlen:
                    continue
                if (newloc, direction) not in visited:
                    heapq.heappush(nodes, (newheatloss, newloc, direction))
    return node[0]

print(getminheatloss(1, 3))
print(getminheatloss(4, 10))
