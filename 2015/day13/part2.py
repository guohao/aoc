import itertools
import math
import sys
from collections import defaultdict

ps = defaultdict(lambda: defaultdict(int))
lines = [line.strip() for line in sys.stdin.readlines()]
for line in lines:
    cs = line.split()
    ps[cs[0]][cs[-1][:-1]] = (-1 if cs[2] == 'lose' else 1) * int(cs[3])

r = - math.inf
for a in itertools.permutations(list(ps.keys()) + ["I"]):
    r = max(sum(ps[a[i]][a[(i - 1) % len(a)]] + ps[a[i]][a[(i + 1) % len(a)]] for i in range(len(a))), r)
print(r)
