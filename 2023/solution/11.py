import sys
from itertools import combinations

with open(sys.argv[1] if len(sys.argv) > 1 else '../input/11') as f:
    image = f.read().splitlines()

rows = [r for r, row in enumerate(image) if '#' not in row]
cols = [c for c, col in enumerate(zip(*image)) if '#' not in col]

galaxys = ((c, r) for r, row in enumerate(image)
        for c, point in enumerate(row) if point == '#')

total = 0
expand = 0
for a, b in combinations(galaxys, 2):
    min_col, max_col = sorted((a[0], b[0]))
    min_row, max_row = sorted((a[1], b[1]))
    total += max_col - min_col + max_row - min_row
    expand += sum(min_col < col < max_col for col in cols)
    expand += sum(min_row < row < max_row for row in rows)
print(total + expand)
print(total + expand*999999)
