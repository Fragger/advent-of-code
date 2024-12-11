import sys
from functools import cache

with open(sys.argv[1] if len(sys.argv) > 1 else '../input/11') as f:
    stones = list(map(int, f.read().split()))

@cache
def splits(n, stone):
    if n == 0:
        return 1
    if stone == 0:
        return splits(n-1, 1)
    if len(str(stone))%2 == 0:
        stone = str(stone)
        return (splits(n-1, int(stone[:len(stone)//2])) +
                splits(n-1, int(stone[len(stone)//2:])))
    return splits(n-1, stone*2024)

print(sum(splits(25, stone) for stone in stones))
print(sum(splits(75, stone) for stone in stones))
