import sys
from itertools import product

p1 = 0
p2 = 0
with open(sys.argv[1] if len(sys.argv) > 1 else '../input/07') as f:
    for line in f:
        test, nums = line.split(':')
        test = int(test)
        nums = tuple(map(int, nums.split()))
        for ops in product(('+', '*', '||'), repeat=len(nums)-1):
            value = nums[0]
            for i, op in enumerate(ops, 1):
                if op == '+':
                    value += nums[i]
                elif op == '*':
                    value *= nums[i]
                elif op == '||':
                    value = int(str(value)+str(nums[i]))
            if value == test:
                if '||' not in ops:
                    p1 += test
                p2 += test
                break
print(p1)
print(p2)
