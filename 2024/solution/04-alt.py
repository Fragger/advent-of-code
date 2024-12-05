import sys

with open(sys.argv[1] if len(sys.argv) > 1 else '../input/04') as f:
    search = f.read().splitlines()

ylen = len(search)
xlen = len(search[0])

find = lambda x, y: search[y][x] if y >= 0 and y < ylen and x >= 0 and x < xlen else None

p1 = 0
p2 = 0
for y in range(ylen):
    for x in range(xlen):
        if search[y][x] == 'X':
            for i, j in ((0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)):
                if (find(x+i, y+j) == 'M' and
                    find(x+i*2, y+j*2) == 'A' and
                    find(x+i*3, y+j*3) == 'S'):
                    p1 += 1
        elif (y >= 1 and y < ylen-1 and x >= 1 and x < xlen-1 and
              search[y][x] == 'A' and
              search[y+1][x+1] in 'MS' and search[y-1][x-1] in 'MS' and search[y+1][x+1] != search[y-1][x-1] and
              search[y+1][x-1] in 'MS' and search[y-1][x+1] in 'MS' and search[y+1][x-1] != search[y-1][x+1]):
            p2 += 1

print(p1)
print(p2)
