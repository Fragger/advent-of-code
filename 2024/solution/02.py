import sys
from itertools import pairwise, combinations

def safe(level):
    diff = [b-a for a, b in pairwise(level)]
    diffmax = max(diff)
    diffmin = min(diff)
    return (diffmax <= 3 and diffmin > 0) or (diffmax < 0 and diffmin >= -3)

p1 = 0
p2 = 0
with open(sys.argv[1] if len(sys.argv) > 1 else '../input/02') as f:
    for levels in f:
        level = list(map(int, levels.split()))
        if safe(level):
            p1 += 1
            p2 += 1
        else:
            for damp in combinations(level, len(level)-1):
                if safe(damp):
                    p2 += 1
                    break

print(p1)
print(p2)
