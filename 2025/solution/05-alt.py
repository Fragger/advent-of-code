import sys

with open(sys.argv[1] if len(sys.argv) > 1 else "../input/05") as f:
    fresh_lines, avail = f.read().split("\n\n")

fresh_ranges = []
for ingredient_range in fresh_lines.splitlines():
    start, stop = map(int, ingredient_range.split("-"))
    fresh_ranges.append(range(start, stop + 1))

p1 = 0
for ingredient in map(int, avail.splitlines()):
    for fresh_range in fresh_ranges:
        if ingredient in fresh_range:
            p1 += 1
            break

current = 0
p2 = 0
fresh_ranges.sort(key=lambda fresh_range: fresh_range.start)
for fresh_range in fresh_ranges:
    current = max(current, fresh_range.start)
    if current < fresh_range.stop:
        p2 += fresh_range.stop - current
        current = fresh_range.stop
    
print(p1)
print(p2)
