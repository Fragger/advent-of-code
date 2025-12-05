import sys

with open(sys.argv[1] if len(sys.argv) > 1 else "../input/05") as f:
    fresh_lines, avail = f.read().split("\n\n")

fresh_ranges = []
for ingredient_range in fresh_lines.splitlines():
    start, stop = map(int, ingredient_range.split("-"))

    new_range = range(start, stop + 1)

    next_fresh_ranges = []
    for fresh_range in fresh_ranges:
        if fresh_range.start < new_range.stop and new_range.start < fresh_range.stop:
            new_range = range(
                min(new_range.start, fresh_range.start),
                max(new_range.stop, fresh_range.stop),
            )
        else:
            next_fresh_ranges.append(fresh_range)
    next_fresh_ranges.append(new_range)
    fresh_ranges = next_fresh_ranges

p1 = 0
for ingredient in map(int, avail.splitlines()):
    for fresh_range in fresh_ranges:
        if ingredient in fresh_range:
            p1 += 1
            break

print(p1)
print(sum(len(fresh_range) for fresh_range in fresh_ranges))
