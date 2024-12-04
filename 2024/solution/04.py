import sys

with open(sys.argv[1] if len(sys.argv) > 1 else '../input/04') as f:
    search = f.read().splitlines()

ylen = len(search)
xlen = len(search[0])

def findnext(word, loc, step):
    if not word:
        return 1
    loc = loc[0]+step[0], loc[1]+step[1]
    if loc[1] >= 0 and loc[1] < ylen and loc[0] >= 0 and loc[0] < xlen and search[loc[1]][loc[0]] == word[0]:
        return findnext(word[1:], loc, step)

    return 0

p1 = 0
p2 = 0
for y in range(ylen):
    for x in range(xlen):
        if search[y][x] == 'X':
            for step in ((0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)):
                p1 += findnext('MAS', (x, y), step)
        if (y >= 1 and y < ylen-1 and x >= 1 and x < xlen-1 and
            search[y][x] == 'A' and
            search[y+1][x+1] in 'MS' and search[y-1][x-1] in 'MS' and search[y+1][x+1] != search[y-1][x-1] and
            search[y+1][x-1] in 'MS' and search[y-1][x+1] in 'MS' and search[y+1][x-1] != search[y-1][x+1]):
            p2 += 1

print(p1)
print(p2)
