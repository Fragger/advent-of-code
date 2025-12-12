import sys
from math import sumprod

with open(sys.argv[1] if len(sys.argv) > 1 else "../input/12") as f:
    *presents, regions = f.read().split("\n\n")

presents = [present.count("#") for present in presents]

p1 = 0
for region in regions.splitlines():
    size, pcounts = region.split(":")
    width, length = map(int, size.split("x"))
    pcounts = map(int, pcounts.split())

    p1 += width * length >= sumprod(presents, pcounts)

print(p1)
