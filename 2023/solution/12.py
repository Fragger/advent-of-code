import sys
from functools import cache

@cache
def arrange(records, sizes, damaged = 0):
    match records[:1], damaged:
        case '', 0:
            if not sizes:
                # consumed all sizes and no current damaged count
                return 1
        case '', _:
            if len(sizes) == 1 and sizes[0] == damaged:
                # one size left and it equals the damaged count we have
                return 1
        case '?', 0:
            return (arrange(records[1:], sizes) + 
                    # count as .
                    arrange(records[1:], sizes, damaged + 1))
                    #count as #
        case '?', _:
            if sizes:
                if sizes[0] == damaged:
                    return arrange(records[1:], sizes[1:])
                    # count as . consume one size since we had the correct count of # 
                    # can't count as #
                else:
                    return arrange(records[1:], sizes, damaged + 1)
                    # count as # can't count as .
        case '#', _:
            if sizes and sizes[0] != damaged:
                return arrange(records[1:], sizes, damaged + 1)
                # still have more damaged to count on current size
        case '.', 0:
            return arrange(records[1:], sizes)
            # next record
        case '.', _:
            if sizes and sizes[0] == damaged:
                return arrange(records[1:], sizes[1:]) 
                # consume one size since we had the correct count of #

    return 0

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
