import sys

def calc(ax, ay, bx, by, prizex, prizey):
    #ax*i+bx*j=prizex
    #ay*i+by*j=prizey
    det = ax*by-bx*ay

    i = (by*prizex-bx*prizey)//det
    j = (-ay*prizex+ax*prizey)//det

    if ax*i+bx*j == prizex and ay*i+by*j == prizey:
        return i*3+j
    return 0

p1 = 0
p2 = 0
with open(sys.argv[1] if len(sys.argv) > 1 else '../input/13') as f:
    for machine in f.read().split('\n\n'):
        (ax, ay), (bx, by), (prizex, prizey) = ((int(n.strip()[2:])
                                                 for n in line.split(':')[1].split(','))
                                                for line in machine.splitlines())
        p1 += calc(ax, ay, bx, by, prizex, prizey)

        prizex += 10000000000000
        prizey += 10000000000000
        p2 += calc(ax, ay, bx, by, prizex, prizey)
print(p1)
print(p2)
