import sys

#      --------Part 1--------   --------Part 2--------
#Day       Time   Rank  Score       Time   Rank  Score
# 18   00:16:28    533      0   00:20:08     90     11

p1prev = (0, 0)
p2prev = (0, 0)
p1 = 0
p2 = 0
p1totaldist = 0
p2totaldist = 0

head = {'U': (0, -1),
        'D': (0, 1),
        'R': (1, 0),
        'L': (-1, 0)}

add_point = lambda a, b: (a[0] + b[0], a[1] + b[1])
mult_point = lambda point, mult: (point[0]*mult, point[1]*mult)
determinant = lambda a, b: a[0]*b[1] - b[0]*a[1]

with open(sys.argv[1] if len(sys.argv) > 1 else '../input/18') as f:
    for line in f:
        p1dig, p1dist, color = line.split()
        p1dist = int(p1dist)
        p2dig = 'RDLU'[int(color[-2])]
        p2dist = int(color[2:-2], 16)

        p1cur = add_point(p1prev, mult_point(head[p1dig], p1dist))
        p2cur = add_point(p2prev, mult_point(head[p2dig], p2dist))

        p1 += determinant(p1prev, p1cur)
        p2 += determinant(p2prev, p2cur)
        p1totaldist += p1dist
        p2totaldist += p2dist
        p1prev = p1cur
        p2prev = p2cur

print(p1//2 + p1totaldist//2 + 1)
print(p2//2 + p2totaldist//2 + 1)
