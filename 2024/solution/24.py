import sys
from collections import deque
from operator import and_, or_, xor

with open(sys.argv[1] if len(sys.argv) > 1 else '../input/24') as f:
    inputlines, gatelines = f.read().split('\n\n')

inputs = {name: int(value) for name, value in (line.split(': ') for line in inputlines.splitlines())}

outputs = {}
revoutputs = {}
gates = deque([])
for line in gatelines.splitlines():
    ingate, output = line.split(' -> ')
    ina, gate, inb = ingate.split()
    gates.append((ina, gate, inb, output))
    outputs[output] = (gate, frozenset({ina, inb}))
    revoutputs[(gate, frozenset({ina, inb}))] = output

while gates:
    ina, gate, inb, output = gates.popleft()
    if ina in inputs and inb in inputs:
        inputs[output] = {'AND': and_, 'OR': or_, 'XOR': xor}[gate](inputs[ina], inputs[inb])
    else:
        gates.append((ina, gate, inb, output))

print(sum(value<<int(key[1:]) for key, value in inputs.items() if key[0] == 'z'))

swapped = set()
def swap_outputs(a, b):
    swapped.update({a, b})
    outputs[a], outputs[b] = outputs[b], outputs[a]
    revoutputs[outputs[a]], revoutputs[outputs[b]] = revoutputs[outputs[b]], revoutputs[outputs[a]]

assert outputs['z00'] == ('XOR', frozenset({'y00', 'x00'}))
prevcarry = revoutputs[('AND', frozenset({'y00', 'x00'}))]
for i in sorted(key[1:] for key in inputs if key[0] == 'x' and key != 'x00'):
    pzi = ('XOR', frozenset({'y'+i, 'x'+i}))

    zi = ('XOR', frozenset({prevcarry, revoutputs[pzi]}))
    if outputs['z'+i] != zi:
        if outputs['z'+i][0] != 'XOR':
            swap_outputs('z'+i, revoutputs[zi])
        else:
            swap_outputs(*outputs['z'+i][1]^zi[1])

    partcarry = {revoutputs[('AND', frozenset({'y'+i, 'x'+i}))]}
    partcarry.add(revoutputs[('AND', frozenset({prevcarry, revoutputs[pzi]}))])
    prevcarry = revoutputs[('OR', frozenset(partcarry))]
assert prevcarry == max(key for key in inputs if key[0] == 'z')

print(','.join(sorted(swapped)))
