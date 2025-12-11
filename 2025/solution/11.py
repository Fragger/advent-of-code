import sys
from functools import cache

cables = {}


@cache
def trace(dev, dac=False, fft=False):
    if dev == "out":
        return dac and fft
    if dev == "dac":
        dac = True
    elif dev == "fft":
        fft = True
    return sum(trace(path, dac, fft) for path in cables[dev])


with open(sys.argv[1] if len(sys.argv) > 1 else "../input/11") as f:
    for line in f:
        dev, outs = line.split(": ")
        cables[dev] = outs.split()

print(trace("you", True, True))
print(trace("svr"))
