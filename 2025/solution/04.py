import sys

with open(sys.argv[1] if len(sys.argv) > 1 else "../input/04") as f:
    grid = {
        (x, y): char
        for y, line in enumerate(f.read().splitlines())
        for x, char in enumerate(line)
    }

p1 = 0
removed = set()
toremove = set()
while toremove or not p1:
    toremove = set()
    for (x, y), char in grid.items():
        if char == "@" and (x, y) not in removed:
            if (
                sum(
                    grid.get((x + i, y + j)) == "@" and (x + i, y + j) not in removed
                    for i in (-1, 0, 1)
                    for j in (-1, 0, 1)
                )
                <= 4
            ):
                toremove.add((x, y))
    if not removed:
        p1 = len(toremove)
    removed.update(toremove)

print(p1)
print(len(removed))
