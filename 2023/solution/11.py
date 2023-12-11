import sys
from itertools import accumulate, combinations

with open(sys.argv[1] if len(sys.argv) > 1 else '../input/11') as f:
    image = f.read().splitlines()

rows = list(accumulate('#' not in row for row in image))
cols = list(accumulate('#' not in col for col in zip(*image)))

galaxies = ((c, r) for r, row in enumerate(image)
        for c, point in enumerate(row) if point == '#')

total = 0
expand = 0
for (a_col, a_row), (b_col, b_row) in combinations(galaxies, 2):
    min_col, max_col = sorted((a_col, b_col))
    min_row, max_row = sorted((a_row, b_row))
    total += max_col - min_col + max_row - min_row
    expand += cols[max_col] - cols[min_col] + rows[max_row] - rows[min_row]
print(total + expand)
print(total + expand*999999)
