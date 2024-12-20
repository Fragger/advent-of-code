import sys

with open(sys.argv[1] if len(sys.argv) > 1 else '../input/20') as f:
    rt = {(x, y): c for y, line in enumerate(f.read().splitlines()) for x, c in enumerate(line)}

start = next(pos for pos, c in rt.items() if c == 'S')
end = next(pos for pos, c in rt.items() if c == 'E')

path = [start]
prev = ()
while path[-1] != end:
    x, y = path[-1]
    for dx, dy in (0, -1), (1, 0), (0, 1), (-1, 0):
        nxy = x+dx, y+dy
        if nxy != prev and rt.get(nxy, '#') != '#':
            prev = path[-1]
            path.append(nxy)
            break

path = {loc: dist for dist, loc in enumerate(path)}

p1 = 0
p2 = 0
for dx in range(-20, 21):
    for dy in range(-20, 21):
        cheat = abs(dx)+abs(dy)
        if cheat < 2 or cheat > 20:
            continue
        for sx, sy in path:
            if (sx+dx, sy+dy) in path and path[sx+dx, sy+dy]-path[sx, sy]-cheat >= 100:
                if cheat == 2:
                    p1 += 1
                p2 += 1
print(p1)
print(p2)
