import sys
from collections import deque

parts = sys.stdin.read().split('\n\n')
seeds = list(map(int, parts[0].split(':')[1].split()))
parts = [part.splitlines()[1:] for part in parts[1:]]
seeds = deque([(seeds[i], seeds[i + 1]) for i in range(0, len(seeds), 2)])
for mappings in parts:
    ns = deque()
    while seeds:
        ss, srl = seeds.popleft()
        for m in mappings:
            ts, fs, mrl = map(int, m.split())
            if fs <= ss < fs + mrl:
                ns.append((ts + ss - fs, min(ss + srl, fs + mrl) - ss))
                if ss + srl > fs + mrl:
                    seeds.append((fs + mrl, ss + srl - fs - mrl))
                break
    seeds = ns

print(sorted(seeds)[0][0])
