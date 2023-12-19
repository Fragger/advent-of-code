import sys
from collections import defaultdict, namedtuple

with open(sys.argv[1] if len(sys.argv) > 1 else '../input/19') as f:
    workflowlines, parts = f.read().split('\n\n')

Rule = namedtuple('Rule', ('cat', 'op', 'val', 'dest'))
workflows = defaultdict(list)
for workflow in workflowlines.splitlines():
    name, rules = workflow[:-1].split('{')
    for rule in rules.split(','):
        if ':' not in rule:
            workflows[name].append(rule)
        else:
            rule, dest = rule.split(':')
            workflows[name].append(Rule(rule[0], rule[1], int(rule[2:]), dest))

p1sum = 0
for part in parts.splitlines():
    xmas = {}
    for rating in part[1:-1].split(','):
        cat, val = rating.split('=')
        xmas[cat] = int(val)

    workflow = 'in'
    while workflow not in 'RA':
        for rule in workflows[workflow]:
            if isinstance(rule, str):
                workflow = rule
                break
            if rule.op == '>':
               if xmas[rule.cat] > rule.val:
                   workflow = rule.dest
                   break
            elif rule.op == '<':
               if xmas[rule.cat] < rule.val:
                   workflow = rule.dest
                   break
    if workflow == 'A':
        p1sum += sum(xmas.values())
print(p1sum)

ranges = [('in', {cat: range(1, 4001) for cat in 'xmas'})]
p2comb = 0
while ranges:
    workflow, xmas = ranges.pop()
    if workflow == 'A':
        comb = 1
        for rating in xmas.values():
            comb *= rating.stop - rating.start
        p2comb += comb
        continue
    if workflow == 'R':
        continue
    for rule in workflows[workflow]:
        if isinstance(rule, str):
            ranges.append((rule, xmas))
            break
        if rule.op == '>':
            if xmas[rule.cat].start > rule.val:
                ranges.append((rule.dest, xmas))
                break
            if xmas[rule.cat].stop > rule.val+1:
                ranges.append((rule.dest,
                    xmas | {rule.cat: range(rule.val+1, xmas[rule.cat].stop)}))
                xmas[rule.cat] = range(xmas[rule.cat].start, rule.val+1)
        elif rule.op == '<':
            if xmas[rule.cat].stop <= rule.val:
                ranges.append((rule.dest, xmas))
                break
            if xmas[rule.cat].start < rule.val:
                ranges.append((rule.dest,
                    xmas | {rule.cat: range(xmas[rule.cat].start, rule.val)}))
                xmas[rule.cat] = range(rule.val, xmas[rule.cat].stop)
print(p2comb)
