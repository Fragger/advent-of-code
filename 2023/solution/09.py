import sys
from itertools import pairwise

p1sum = 0
p2sum = 0
with open(sys.argv[1] if len(sys.argv) > 1 else '../input/09') as f:
    for line in f:
        diff = [int(num) for num in line.split()]
        diff2 = diff[::-1]
        while any(diff):
            p1sum += diff[-1]
            p2sum += diff2[-1]
            diff = [b - a for a, b in pairwise(diff)]
            diff2 = [b - a for a, b in pairwise(diff2)]

print(p1sum)
print(p2sum)
