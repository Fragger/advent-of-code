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
    new_circuits = [{a, b}]
    for circuit in circuits:
        if not circuit.isdisjoint(new_circuits[0]):
            new_circuits[0].update(circuit)
        else:
            new_circuits.append(circuit)

    circuits = new_circuits

    if conn_count == 1000:
        circuits.sort(reverse=True, key=len)
        print(reduce(mul, map(len, circuits[:3])))

    if len(circuits[0]) == len_boxes:
        print(a[0] * b[0])
        break
