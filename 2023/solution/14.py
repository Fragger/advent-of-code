import sys

def printsum(state):
    print(sum(row.count('O')*(i + 1) for i, row in enumerate(state[::-1])))

with open(sys.argv[1] if len(sys.argv) > 1 else '../input/14') as f:
    platform = tuple(tuple(line.strip()) for line in f)

seen = []
while platform not in seen:
    seen.append(platform)

    for i in range(4):
        platform = tuple(
                tuple('#'.join(
                    ''.join(sorted(sub, reverse=i<2)) for sub in ''.join(line).split('#')
                )) for line in zip(*platform))

        if len(seen) == 1 and i == 0:
            printsum(tuple(zip(*platform)))

offset = seen.index(platform)
cycle = len(seen)-offset
index = (1000000000-offset)%cycle+offset

printsum(seen[index])
