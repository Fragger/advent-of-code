import sys

locks = []
keys = []
with open(sys.argv[1] if len(sys.argv) > 1 else '../input/25') as f:
    for sch in f.read().split('\n\n'):
        sch = list(sch.splitlines())
        if sch[0][0] == '#':
            locks.append([sum(sch[y][x] == '#' for y in range(1, len(sch))) for x in range(len(sch[0]))])
        else:
            keys.append([sum(sch[y][x] == '#' for y in range(0, len(sch)-1)) for x in range(len(sch[0]))])

print(sum(all(k+l <= 5 for k, l in zip(key, lock)) for key in keys for lock in locks))
