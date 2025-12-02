import re
import sys

p1 = 0
p2 = 0
check1 = re.compile(r"(.+)\1")
check2 = re.compile(r"(.+)\1+")
with open(sys.argv[1] if len(sys.argv) > 1 else "../input/02") as f:
    for idrange in f.read().split(","):
        first, last = idrange.split("-")
        for num in range(int(first), int(last) + 1):
            if check2.fullmatch(str(num)):
                if check1.fullmatch(str(num)):
                    p1 += num
                p2 += num

print(p1)
print(p2)
