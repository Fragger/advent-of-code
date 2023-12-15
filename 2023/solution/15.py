import sys
from collections import defaultdict

with open(sys.argv[1] if len(sys.argv) > 1 else '../input/15') as f:
    sequence = f.read().strip().split(',')

def calc(chars):
    value = 0
    for char in chars:
        value += ord(char)
        value *= 17
        value %= 256
    return value

p1sum = 0
boxes = defaultdict(dict)
for step in sequence:
    p1sum += calc(step)

    if step[-2] == '=':
        label, fl = step.split('=')
        boxes[calc(label)][label] = int(fl)
    elif step[-1] == '-':
        label = step[:-1]
        boxes[calc(label)].pop(label, None)

print(p1sum)

print(sum((box + 1) * (slot + 1) * fl
    for box, lenses in boxes.items()
    for slot, fl in enumerate(lenses.values())))
