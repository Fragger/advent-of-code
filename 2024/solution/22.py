import sys
from collections import Counter

p1 = 0
sequences = Counter()
with open(sys.argv[1] if len(sys.argv) > 1 else '../input/22') as f:
    for secret in f:
        secret = int(secret)
        last = secret%10
        changes = []
        seen = set()
        for _ in range(2000):
            secret ^= secret*64
            secret %= 16777216
            secret ^= secret//32
            secret %= 16777216
            secret ^= secret*2048
            secret %= 16777216
            price = secret%10
            diff = price-last
            last = price
            changes.append(diff)
            if len(changes) >= 4:
                seq = tuple(changes[-4:])
                if seq not in seen:
                    seen.add(seq)
                    sequences[seq] += price
        p1 += secret

print(p1)
print(sequences.most_common(1)[0][1])
