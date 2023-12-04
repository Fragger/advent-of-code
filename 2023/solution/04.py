import sys
from collections import defaultdict

p1sum = 0
p2cardcount = defaultdict(int)

with open(sys.argv[1] if len(sys.argv) > 1 else '../input/04') as f:
    for i, line in enumerate(f):
        left, right = [set(part.split()) for part in line.split(':')[1].split('|')]
        wins = len(left & right)
        if wins:
            p1sum += 2**(wins-1)
        p2cardcount[i] += 1
        for j in range(wins):
            p2cardcount[i+j+1] += p2cardcount[i]

print(p1sum)
print(sum(p2cardcount.values()))
