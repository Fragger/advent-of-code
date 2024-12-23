import sys
from collections import defaultdict

conns = defaultdict(set)
with open(sys.argv[1] if len(sys.argv) > 1 else '../input/23') as f:
    for line in f.read().splitlines():
        comp_a, comp_b = line.split('-')
        conns[comp_a].add(comp_b)
        conns[comp_b].add(comp_a)

groups = set()
stack = [(comp, frozenset({comp})) for comp in conns]
while stack:
    comp, group = stack.pop()
    for conn_comp in conns[comp]-group:
        if conns[conn_comp] >= group:
            new_group = group|{conn_comp}
            if new_group not in groups:
                groups.add(new_group)
                stack.append((conn_comp, new_group))

print(sum(len(group) == 3 and any(comp[0] == 't' for comp in group) for group in groups))
print(','.join(sorted(max(groups, key=len))))
