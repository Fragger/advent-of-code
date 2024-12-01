import sys
from collections import Counter

leftlist = []
rightlist = []
with open(sys.argv[1] if len(sys.argv) > 1 else '../input/01') as f:
    for line in f:
        left, right = line.split()
        leftlist.append(int(left))
        rightlist.append(int(right))

p1sum = 0
p2sum = 0
rightcount = Counter(rightlist)
for left, right in zip(sorted(leftlist), sorted(rightlist)):
    p1sum += abs(left-right)
    p2sum += left * rightcount[left]

print(p1sum)
print(p2sum)
