import sys
import re

with open(sys.argv[1] if len(sys.argv) > 1 else '../input/03') as f:
    memory = f.read()

p1 = 0
p2 = 0
mulenabled = True
for match in re.finditer(r"mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\)", memory):
    instr = match.group(0)
    if instr.startswith('mul'):
        x, y = map(int, match.groups())
        p1 += x*y
        if mulenabled:
            p2 += x*y
    elif instr == 'do()':
        mulenabled = True
    elif instr == "don't()":
        mulenabled = False

print(p1)
print(p2)
