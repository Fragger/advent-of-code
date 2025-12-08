import sys
from collections import Counter
from functools import reduce
from itertools import combinations
from math import dist
from operator import itemgetter, mul

with open(sys.argv[1] if len(sys.argv) > 1 else "../input/08") as f:
    boxes = [tuple(map(int, line.strip().split(","))) for line in f]

len_boxes = len(boxes)
connections = sorted(
    combinations(range(len_boxes), 2),
    key=lambda conn: dist(boxes[conn[0]], boxes[conn[1]]),
)


circuits = list(range(len_boxes))


def find(x):
    if x == circuits[x]:
        return x
    circuits[x] = find(circuits[x])
    return circuits[x]


joined = 0
for conn_count, (a, b) in enumerate(connections, 1):
    if find(a) != find(b):
        joined += 1
        if joined == len_boxes - 1:
            print(boxes[a][0] * boxes[b][0])
            break
        circuits[find(a)] = find(b)

    if conn_count == 1000:
        c_sizes = Counter(find(box) for box in range(len_boxes))
        print(reduce(mul, map(itemgetter(1), c_sizes.most_common(3))))
