import sys
from collections import Counter

with open(sys.argv[1] if len(sys.argv) > 1 else '../input/10') as f:
    topo = {(x, y): int(h) for y, line in enumerate(f.read().splitlines()) for x, h in enumerate(line)}

def step(ans, h, loc):
    if loc in topo and h == topo[loc]:
        if h == 9:
            ans[loc] += 1
        else:
            for x, y in ((0, -1), (1, 0), (0, 1), (-1, 0)):
                step(ans, h+1, (loc[0]+x, loc[1]+y))
    return ans

trails = [step(Counter(), 0, loc) for loc, h in topo.items() if h == 0]

print(sum(len(trail) for trail in trails))
print(sum(trail.total() for trail in trails))
