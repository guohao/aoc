import itertools
import math
from collections import defaultdict

ps = defaultdict(lambda: defaultdict(int))

try:
    while True:
        cs = input().split()
        ps[cs[0]][cs[-1][:-1]] = (-1 if cs[2] == 'lose' else 1) * int(cs[3])
except EOFError:
    pass

r = - math.inf
for a in itertools.permutations(list(ps.keys()) + ["I"]):
    r = max(sum(ps[a[i]][a[(i - 1) % len(a)]] + ps[a[i]][a[(i + 1) % len(a)]] for i in range(len(a))), r)
print(r)
