import sys

p1 = 0
p2 = 0
with open(sys.argv[1] if len(sys.argv) > 1 else "../input/02") as f:
    for idrange in f.read().split(","):
        first, last = idrange.split("-")
        for num in range(int(first), int(last) + 1):
            snum = str(num)
            num_len = len(snum)
            for size in reversed(range(1, num_len // 2 + 1)):
                if num_len % size == 0:
                    for i in range(size, num_len, size):
                        if snum[:size] != snum[i : i + size]:
                            break
                    else:
                        if size == num_len / 2:
                            p1 += num
                        p2 += num
                        break

print(p1)
print(p2)
