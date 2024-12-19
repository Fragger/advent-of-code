import sys
from functools import cache

with open(sys.argv[1] if len(sys.argv) > 1 else '../input/19') as f:
    towels, designs = f.read().split('\n\n')

towels = towels.split(', ')
designs = designs.splitlines()

@cache
def match(design):
    if not design:
        return 1
    designs = 0
    for towel in towels:
        len_towel = len(towel)
        if design[:len_towel] == towel:
            designs += match(design[len_towel:])
    return designs

arrangements = list(map(match, designs))
print(len(list(filter(None, arrangements))))
print(sum(arrangements))
