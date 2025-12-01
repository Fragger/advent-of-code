import sys
from operator import add, sub

opr = {"R": add, "L": sub}
with open(sys.argv[1] if len(sys.argv) > 1 else "../input/01") as f:
    dial = 50
    p1 = 0
    p2 = 0
    for line in f:
        move = int(line[1:])

        p2 += (opr[line[0]](100, dial) % 100 + move) // 100

        dial = opr[line[0]](dial, move) % 100

        if dial == 0:
            p1 += 1

print(p1)
print(p2)
