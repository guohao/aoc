import sys

parts = sys.stdin.read().split('\n\n')
seeds = list(map(int, parts[0].split(':')[1].split()))
parts = [part.splitlines()[1:] for part in parts[1:]]
ans = []
for s in seeds:
    for mappings in parts:
        for m in mappings:
            ts, fs, rl = map(int, m.split())
            if fs <= s < fs + rl:
                s = ts + s - fs
                break
    else:
        ans.append(s)

print(sorted(ans)[0])
