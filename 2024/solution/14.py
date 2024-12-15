import sys

tilesx = 101
tilesy = 103

with open(sys.argv[1] if len(sys.argv) > 1 else '../input/14') as f:
    robots = [tuple(tuple(int(n)
                          for n in cord[2:].split(','))
                    for cord in robot.split())
              for robot in f.read().splitlines()]

safetyfactors = []
for t in range(max(tilesx, tilesy)):
    quads = [0, 0, 0, 0]
    for ((px, py), (vx, vy)) in robots:
        x = (px+vx*t)%tilesx
        y = (py+vy*t)%tilesy
        if x != tilesx//2 and y != tilesy//2:
            x = x//(tilesx//2+1)
            y = y//(tilesy//2+1)
            quads[y*2+x] += 1
    safetyfactor = 1
    for quad in quads:
        safetyfactor *= quad
    safetyfactors.append((safetyfactor, t, quads))

for _, t, quads in sorted(safetyfactors)[:2]:
    if quads[0] > len(robots)//4 < quads[2] or quads[1] > len(robots)//4 < quads[3]:
        tx = t
    else:
        ty = t

p2 = tx+(pow(tilesx, -1, tilesy)*(ty-tx))%tilesy*tilesx # Chinese Remainder Theorem

locs = set()
for ((px, py), (vx, vy)) in robots:
    x = (px+vx*p2)%tilesx
    y = (py+vy*p2)%tilesy
    locs.add((x, y))
print('\n'.join(''.join('#' if (x, y) in locs else ' ' for x in range(tilesx)) for y in range(tilesy)))

print(safetyfactors[100][0])
print(p2)
