import re

import io_utils

data = io_utils.get_data(2023, 5)
parts = data.split('\n\n')
seeds = list(map(int, parts[0].split()[1:]))
mappings = parts[1:]
for mapping in mappings:
    epoch = []
    for line in mapping.splitlines()[1:]:
        d, s, r = map(int, re.match(r'(\d+) (\d+) (\d+)', line).groups())
        for seed in seeds.copy():
            if s <= seed < s + r:
                seeds.remove(seed)
                epoch.append(d + seed - s)
    seeds += epoch
print(min(seeds))
sr = list(map(int, parts[0].split()[1:]))
seeds = set((sr[i], sr[i] + sr[i + 1]) for i in range(0, len(sr), 2))
print(seeds)

for mapping in mappings:
    epoch = set()
    for line in mapping.splitlines()[1:]:
        d, s, r = map(int, re.match(r'(\d+) (\d+) (\d+)', line).groups())
        for lo, hi in seeds.copy():
            if (s + r - lo) * (s - hi) < 0:
                seeds.remove((lo, hi))
                epoch.add((d + max(0, lo - s), d + min(hi - s, s + r)))
                if lo < s:
                    seeds.add((lo, s))
                if hi > s + r:
                    seeds.add((s + r, hi))
    seeds = seeds.union(epoch)
print(min(seeds)[0])
