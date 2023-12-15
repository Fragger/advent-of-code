import sys
from collections import defaultdict

def arrange(records, sizes):
    perms = defaultdict(int)
    perms[(0, 0)] = 1 # size index, damaged count = num perms
    for char in records:
        perms_next = defaultdict(int)
        for (size, damaged), count in perms.items():
            if char in '.?':
                if damaged == 0:
                    # next
                    perms_next[(size, 0)] += count
                elif sizes[size] == damaged:
                    # consume one size since we had the correct count of #
                    perms_next[(size + 1, 0)] += count
            if char in '#?' and size < len(sizes) and sizes[size] != damaged:
                # still have more damaged to count on current size
                perms_next[(size, damaged + 1)] += count
        perms = perms_next

    # sum count where we have consumed all sizes or
    #   there is one size left and it equals the damaged count we have
    return sum(
        count
        for (size, damaged), count in perms.items()
        if size == len(sizes) or size + 1 == len(sizes) and sizes[size] == damaged
    )

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
