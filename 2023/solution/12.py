import sys
from functools import cache

def arrange(records, sizes):
    @cache
    def _arrange(record, size, damaged = 0):
        if record == len(records):
            if size == len(sizes):
                # consumed all sizes
                return 1
            elif size + 1 == len(sizes) and sizes[size] == damaged:
                # one size left and it equals the damaged count we have
                return 1
            else:
                return 0
        ans = 0
        if records[record] in '.?':
            if damaged == 0:
                # next record
                ans += _arrange(record + 1, size)
            elif sizes[size] == damaged:
                # consume one size since we had the correct count of #
                ans += _arrange(record + 1, size + 1)
        if records[record] in '#?' and size < len(sizes) and sizes[size] != damaged:
            # still have more damaged to count on current size
            ans += _arrange(record + 1, size, damaged + 1)
        return ans
    return _arrange(0, 0)

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
