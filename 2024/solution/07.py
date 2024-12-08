import sys
from itertools import product
from math import log10
from operator import add, mul

def concat(a, b):
    return a*10**(int(log10(b))+1)+b

p1 = 0
p2 = 0
with open(sys.argv[1] if len(sys.argv) > 1 else '../input/07') as f:
    for line in f:
        test, nums = line.split(':')
        test = int(test)
        nums = tuple(map(int, nums.split()))
        for ops in product((add, mul, concat), repeat=len(nums)-1):
            value = nums[0]
            for num, op in zip(nums[1:], ops):
                value = op(value, num)
            if value == test:
                if concat not in ops:
                    p1 += test
                p2 += test
                break
print(p1)
print(p2)
