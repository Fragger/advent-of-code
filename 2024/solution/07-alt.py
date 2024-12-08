import sys
from math import log10
from operator import add, mul

def concat(a, b):
    return a*10**(int(log10(b))+1)+b

def calibrate(test, value, i, nums, p2flag=False):
    if i == len(nums) or value > test:
        return value == test, p2flag

    for op in (add, mul, concat):
        result = calibrate(test, op(value, nums[i]), i+1, nums, (p2flag or op == concat))
        if result[0]:
            return result

    return False, p2flag

p1 = 0
p2 = 0
with open(sys.argv[1] if len(sys.argv) > 1 else '../input/07') as f:
    for line in f:
        test, nums = line.split(':')
        test = int(test)
        nums = tuple(map(int, nums.split()))

        result, p2flag = calibrate(test, nums[0], 1, nums)

        p1 += test*(result and not p2flag)
        p2 += test*result
print(p1)
print(p2)
