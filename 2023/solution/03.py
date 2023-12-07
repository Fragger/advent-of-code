import sys
from collections import defaultdict

with open(sys.argv[1] if len(sys.argv) > 1 else '../input/03') as f:
    schematic = f.read().splitlines()
    p1sum = 0
    p2stars = defaultdict(list)
    for i, line in enumerate(schematic):
        j = 0
        while j < len(line):
            if line[j].isdigit():
                part = False
                k = j
                while k + 1 < len(line) and line[k + 1].isdigit():
                    k += 1
                for checkline in range(max(0, i-1), min(len(schematic), i+2)):
                    for pos in range(max(0, j-1), min(len(line), k+2)):
                        char = schematic[checkline][pos]
                        if not char.isdigit() and char != '.':
                            part = True
                        if char == '*':
                            p2stars[(checkline, pos)].append(int(line[j:k+1]))
                if part:
                    p1sum += int(line[j:k+1])

                j = k + 1
            else:
                j += 1

print(p1sum)

p2sum = 0
for stars in p2stars.values():
    if len(stars) == 2:
        p2sum += stars[0] * stars[1]
print(p2sum)
