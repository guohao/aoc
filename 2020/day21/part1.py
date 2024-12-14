from collections import defaultdict, Counter
from functools import reduce

import sys

data = sys.stdin.read().strip()

a2i = defaultdict(list)
c = Counter()
for line in data.strip().splitlines():
    l, r = line.split('(contains ')
    l = l.split()
    r = r[:-1].split(', ')
    for x in r:
        a2i[x].append(l)
    c.update(l)
mapping = {}
while len(a2i) != len(mapping):
    for a in set(a2i) - set(mapping):
        common = reduce(lambda a, b: a & b, map(set, a2i[a]))
        if len(common) != 1:
            continue
        ing = list(common)[0]
        mapping[a] = ing
        for k, v in a2i.items():
            for i in range(len(v)):
                if ing in v[i]:
                    a2i[k][i].remove(ing)
for x in mapping.values():
    del c[x]
print(sum(c.values()))
