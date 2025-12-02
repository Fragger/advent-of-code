import sys

p1 = 0
p2 = 0
with open(sys.argv[1] if len(sys.argv) > 1 else "../input/02") as f:
    for idrange in f.read().split(","):
        first, last = idrange.split("-")
        for num in range(int(first), int(last) + 1):
            snum = str(num)
            if snum in (snum * 2)[1:-1]:
                mid = len(snum) // 2
                if snum[:mid] == snum[mid:]:
                    p1 += num
                p2 += num

print(p1)
print(p2)
