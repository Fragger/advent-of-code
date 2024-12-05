import sys
from collections import defaultdict

with open(sys.argv[1] if len(sys.argv) > 1 else '../input/05') as f:
    po, updates = f.read().split('\n\n')

rules = defaultdict(set)
for rule in po.splitlines():
    first, second = rule.split('|')
    rules[first].add(second)

p1 = 0
p2 = 0
for update in updates.splitlines():
    pages = update.split(',')
    incorrect = False
    for i in range(len(pages)):
        while True:
            for j in range(i+1, len(pages)):
                if pages[j] not in rules[pages[i]]:
                    incorrect = True
                    pages = pages[:i] + pages[j:j+1] + pages[i:j] + pages[j+1:]
                    break
            else:
                break
    if not incorrect:
        p1 += int(pages[len(pages)//2])
    else:
        p2 += int(pages[len(pages)//2])
print(p1)
print(p2)
