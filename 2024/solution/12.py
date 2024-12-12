import sys

with open(sys.argv[1] if len(sys.argv) > 1 else '../input/12') as f:
    plotmap = {(x, y): plot for y, line in enumerate(f.read().splitlines()) for x, plot in enumerate(line)}

painted = set()
def paintregion(plot, x, y, region):
    region.add((x, y))
    painted.add((x, y))
    for dx, dy in (0, -1), (1, 0), (0, 1), (-1, 0):
        if (x+dx, y+dy) not in painted and plotmap.get((x+dx, y+dy)) == plot:
            paintregion(plot, x+dx, y+dy, region)

p1 = 0
p2 = 0
for (x, y), plot in plotmap.items():
    if (x, y) not in painted:
        region = set()
        paintregion(plot, x, y, region)
        perimeter = set((x+dx, y+dy, dx, dy)
                        for x, y in region
                        for dx, dy in ((0, -1), (1, 0), (0, 1), (-1, 0))
                        if (x+dx, y+dy) not in region)
        p1 += len(region)*len(perimeter)

        sides = 0
        while perimeter:
            sides += 1
            sx, sy, sdx, sdy = perimeter.pop()
            for dx, dy in (sdy, sdx), (-sdy, -sdx):
                x, y = sx+dx, sy+dy
                while (x, y, sdx, sdy) in perimeter:
                    perimeter.remove((x, y, sdx, sdy))
                    x += dx
                    y += dy
        p2 += len(region)*sides

print(p1)
print(p2)
