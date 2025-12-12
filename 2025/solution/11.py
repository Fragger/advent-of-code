import sys
from functools import cache

cables = {}


@cache
def trace(dev, *visit):
    if dev == "out":
        return len(visit) == 0
    visit = [vdev for vdev in visit if vdev != dev]
    return sum(trace(path, *visit) for path in cables[dev])


with open(sys.argv[1] if len(sys.argv) > 1 else "../input/11") as f:
    for line in f:
        dev, outs = line.split(":")
        cables[dev] = outs.split()

print(trace("you"))
print(trace("svr", "dac", "fft"))
