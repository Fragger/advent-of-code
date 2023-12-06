import sys

with open(sys.argv[1] if len(sys.argv) > 1 else '../input/05') as f:
    almanac = f.read().split('\n\n')
seeds = [int(seed) for seed in almanac[0].split(':')[1].split()]

loc = []
for seed in seeds:
    for section in almanac[1:]:
        for mapping in section.splitlines()[1:]:
            dest, source, length = (int(num) for num in mapping.split())
            if source <= seed < source + length:
                seed += dest - source
                break
    loc.append(seed)

print(min(loc))

seeds = [(start, start + length) for start, length in zip(seeds[::2], seeds[1::2])]

for section in almanac[1:]:
    nextseeds = []
    for seed in seeds:
        for mapping in section.splitlines()[1:]:
            dest, source, length = (int(num) for num in mapping.split())
            if seed[0] < source + length and seed[1] > source:
                # [seed[0]                                 seed[1])
                #           [source   source + length)
                # [before  )[middle                  )[after      )

                middle = (max(seed[0], source), min(seed[1], source + length))
                before = (seed[0], middle[0])
                after = (middle[1], seed[1])

                if before[0] < before[1]:
                    seeds.append(before)
                if after[0] < after[1]:
                    seeds.append(after)
                nextseeds.append((middle[0] + dest - source, middle[1] + dest - source))
                break
        else:
            nextseeds.append(seed)
    seeds = nextseeds

print(min(seeds)[0])
