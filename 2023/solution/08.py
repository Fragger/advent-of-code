import sys
from math import lcm

nodes = {}
current = []
with open(sys.argv[1] if len(sys.argv) > 1 else '../input/08') as f:
    directions, network = f.read().split('\n\n')
for node in network.splitlines():
    element, links = node.split(' = ')
    nodes[element] = links[1:-1].split(', ')
    if element.endswith('A'):
        current.append(element)

steps = 0
p1index = current.index('AAA')
z = [0] * len(current)
while not all(z):
    direction = directions[steps%len(directions)]
    for i, element in enumerate(current):
        current[i] = nodes[element]['LR'.index(direction)]
        if element.endswith('Z'):
            z[i] = steps
    steps += 1

print(z[p1index])
print(lcm(*z))
