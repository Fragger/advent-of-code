import sys
from collections import defaultdict
from functools import cache
from itertools import combinations
from math import inf

p1 = 0
p2 = 0
with open(sys.argv[1] if len(sys.argv) > 1 else "../input/10") as f:
    for line in f:
        lights, *buttons, joltages = [item[1:-1] for item in line.split()]
        lights = tuple(light == "#" for light in lights)
        buttons = tuple(set(map(int, button.split(","))) for button in buttons)
        joltages = tuple(map(int, joltages.split(",")))

        parity = defaultdict(list)
        for count in range(len(buttons) + 1):
            for presses in combinations(buttons, count):
                result = tuple(
                    len([1 for button in presses if i in button])
                    for i in range(len(joltages))
                )
                parity[tuple(counter % 2 for counter in result)].append((count, result))

        p1 += min(count for count, _ in parity[lights])

        @cache
        def push_buttons(target):
            if any(counter < 0 for counter in target):
                return inf
            if all(counter == 0 for counter in target):
                return 0

            ans = inf
            for count, result in parity[tuple(counter % 2 for counter in target)]:
                new_target = tuple((t - r) // 2 for t, r in zip(target, result))
                ans = min(ans, count + 2 * push_buttons(new_target))
            return ans

        p2 += push_buttons(joltages)

print(p1)
print(p2)
