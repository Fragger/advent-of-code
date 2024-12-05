import sys
from collections import defaultdict
from functools import cmp_to_key

with open(sys.argv[1] if len(sys.argv) > 1 else '../input/05') as f:
    po, updates = f.read().split('\n\n')

rules = defaultdict(set)
for rule in po.splitlines():
    first, second = rule.split('|')
    rules[first].add(second)

p1 = 0
p2 = 0
for update in updates.splitlines():
    pages = update.split(',')
    sortedpages = sorted(pages, key=cmp_to_key(lambda a, b: 1 if b not in rules[a] else -1))
    if sortedpages == pages:
        p1 += int(pages[len(pages)//2])
    else:
        p2 += int(sortedpages[len(pages)//2])
print(p1)
print(p2)
