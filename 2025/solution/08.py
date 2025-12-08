import sys
from functools import reduce
from itertools import combinations
from math import dist
from operator import mul

with open(sys.argv[1] if len(sys.argv) > 1 else "../input/08") as f:
    boxes = [tuple(map(int, line.strip().split(","))) for line in f]

len_boxes = len(boxes)
connections = sorted(combinations(boxes, 2), key=lambda conn: dist(*conn))

circuits = []
for conn_count, (a, b) in enumerate(connections, 1):
    a_circuit = None
    b_circuit = None
    for i, circuit in enumerate(circuits):
        if a in circuit:
            a_circuit = i
        if b in circuit:
            b_circuit = i

    if a_circuit is None and b_circuit is None:
        circuits.append(set((a, b)))
    elif a_circuit != b_circuit:
        if a_circuit is None:
            circuits[b_circuit].add(a)
        elif b_circuit is None:
            circuits[a_circuit].add(b)
        else:
            circuits[a_circuit].update(circuits[b_circuit])
            del circuits[b_circuit]

    if conn_count == 1000:
        circuits.sort(reverse=True, key=len)
        print(reduce(mul, map(len, circuits[:3])))

    if len(circuits[0]) == len_boxes:
        print(a[0] * b[0])
        break
