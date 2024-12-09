import sys

with open(sys.argv[1] if len(sys.argv) > 1 else '../input/09') as f:
    blocks1 = list(map(int, f.read().strip()))
blocks1.append(0)

blocks2 = []
pos = 0
for block in blocks1:
    blocks2.append([block, pos])
    pos += block

p1 = 0

pos = 0
idnum = 0
free = 0
endidnum = len(blocks1)//2-1
while idnum <= endidnum:
    while blocks1[idnum*2] > 0:
        p1 += pos*idnum
        pos += 1
        blocks1[idnum*2] -= 1
    idnum += 1
    if endidnum > idnum:
        while blocks1[free*2+1] > 0:
            if blocks1[endidnum*2] == 0:
                endidnum -= 1
            p1 += pos*endidnum
            pos += 1
            blocks1[endidnum*2] -= 1
            blocks1[endidnum*2+1] += 1
            blocks1[free*2+1] -= 1
        free += 1
print(p1)

p2 = 0

idnum = len(blocks2)//2-1
while idnum >= 0:
    free = 0
    while free*2+1 < idnum*2:
        if blocks2[free*2+1][0] >= blocks2[idnum*2][0]:
            pos = blocks2[free*2+1][1]
            blocks2[free*2+1][0] -= blocks2[idnum*2][0]
            blocks2[free*2+1][1] += blocks2[idnum*2][0]
            while blocks2[idnum*2][0] > 0:
                p2 += pos*idnum
                pos += 1
                blocks2[idnum*2][0] -= 1
            break
        free += 1
    else:
        pos = blocks2[idnum*2][1]
        while blocks2[idnum*2][0] > 0:
            p2 += pos*idnum
            pos += 1
            blocks2[idnum*2][0] -= 1
    idnum -= 1
print(p2)
