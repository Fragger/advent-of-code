import sys

def check(pattern, diff = 0):
    for i in range(1, len(pattern)):
        if diff == sum(a != b
                for lines in zip(pattern[:i][::-1], pattern[i:])
                for a, b in zip(*lines)):
            return i
    return 0

with open(sys.argv[1] if len(sys.argv) > 1 else '../input/13') as f:
    patterns = f.read().split('\n\n')

p1sum = 0
p2sum = 0
for pattern in patterns:
    pattern = pattern.splitlines()
    
    p1sum += check(list(zip(*pattern)))
    p1sum += check(pattern)*100

    p2sum += check(list(zip(*pattern)), 1)
    p2sum += check(pattern, 1)*100

print(p1sum)
print(p2sum)
