import sys
from math import prod

p1sum = 0
p2sum = 0
with open(sys.argv[1] if len(sys.argv) > 1 else '../input/02') as f:
    for line in f:
        gameid, cubes = line.split(':') 
        p2max = [0, 0, 0]
        possible = True
        for cubeset in cubes.split(';'):
            for cube in cubeset.split(','):
                count, color = cube.split()
                count = int(count)

                i = ('red', 'green', 'blue').index(color)
                p2max[i] = max(p2max[i], count)
                if count > 12 + i:
                    possible = False

        if possible:
            p1sum += int(gameid[5:])
        p2sum += prod(p2max)

print(p1sum)
print(p2sum)
