import itertools
import re
import sys

data = sys.stdin.read().strip()

ps = {}
for line in data.splitlines():
    p, pos = list(map(int, re.findall(r'\d+', line)))
    ps[p] = (pos - 1, 0)
dc = 0
dseq = itertools.cycle(range(1, 101))
while True:
    for p, (pos, score) in ps.items():
        moves = sum(next(dseq) for _ in range(3))
        pos = (pos + moves) % 10
        dc += 3
        score += pos + 1
        ps[p] = (pos, score)
        if score >= 1000:
            print(dc * (sum(s for _, s in ps.values()) - score))
            exit()
