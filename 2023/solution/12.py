import sys
from functools import cache

@cache
def arrange(records, sizes, damaged = 0):
    if not records:
        if not sizes:
            # consumed all sizes
            return 1
        elif len(sizes) == 1 and sizes[0] == damaged:
            # one size left and it equals the damaged count we have
            return 1
        else:
            return 0
    ans = 0
    if records[0] in '.?':
        if damaged == 0:
            # next record
            ans += arrange(records[1:], sizes)
        elif sizes[0] == damaged:
            # consume one size since we had the correct count of #
            ans += arrange(records[1:], sizes[1:])
    if records[0] in '#?' and sizes and sizes[0] != damaged:
        # still have more damaged to count on current size
        ans += arrange(records[1:], sizes, damaged + 1)
    return ans

p1sum = 0
p2sum = 0
with open(sys.argv[1] if len(sys.argv) > 1 else '../input/12') as f:
    for line in f:
        records, sizes = line.split()
        sizes = tuple(int(size) for size in sizes.split(','))

        p1sum += arrange(records, sizes)
        p2sum += arrange('?'.join([records]*5), sizes*5)

print(p1sum)
print(p2sum)
