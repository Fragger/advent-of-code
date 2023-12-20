import sys
from collections import deque
from math import lcm

modules = {}
with open(sys.argv[1] if len(sys.argv) > 1 else '../input/20') as f:
    for line in f:
        module, out = line.strip().split(' -> ')
        out = out.split(', ')
        modules[module[1:]] = {'type': module[0],
                               'out': out,
                               'mem': {}}

for name, module in modules.items():
    for out in module['out']:
        if out == 'rx':
            rxin = name
        elif out in modules and modules[out]['type'] == '&':
            modules[out]['mem'][name] = False

low = 0
high = 0
button = 0
pulses = deque()
def sendout(source, signal):
    for out in modules[source]['out']:
        pulses.append((source, signal, out))

rxinstate = {name: 0 for name in modules[rxin]['mem']}

while not all(rxinstate.values()):
    pulses.append(('button', False, 'roadcaster'))
    button += 1

    while pulses:
        source, signal, dest = pulses.popleft()
        if button <= 1000:
            if signal:
                high += 1
            else:
                low += 1

        if dest == rxin and signal:
            rxinstate[source] = button

        if dest not in modules:
            continue
        if modules[dest]['type'] == 'b':
            sendout(dest, signal)
        elif modules[dest]['type'] == '%':
            if not signal:
                modules[dest]['mem'] = not modules[dest]['mem']
                sendout(dest, modules[dest]['mem'])
        elif modules[dest]['type'] == '&':
            modules[dest]['mem'][source] = signal
            sendout(dest, not all(modules[dest]['mem'].values()))

print(low*high)
print(lcm(*rxinstate.values()))
