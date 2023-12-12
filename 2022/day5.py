import copy
import re
from collections import defaultdict, deque

import helper

data = io_utils.get_data(2022, 5)
bs, ms = data.split("\n\n")
d = defaultdict(deque)
for i, line in enumerate(bs.splitlines()[:-1]):
    for j, c in enumerate(line):
        if len(c.strip()) > 0:
            d[j].appendleft(c)

nd = {}
for j, c in enumerate(bs.splitlines()[-1]):
    if c.isnumeric():
        nd[int(c)] = d[j]

d = copy.deepcopy(nd)
for move in ms.splitlines():
    a, b, c = map(int, re.findall(r'\d+', move))
    for i in range(a):
        d[c].append(d[b].pop())
print(''.join([d[k][-1] for k in sorted(d.keys())]))

d = copy.deepcopy(nd)

for move in ms.splitlines():
    a, b, c = map(int, re.findall(r'\d+', move))
    tmp = [d[b].pop() for i in range(a)]
    tmp.reverse()
    for e in tmp:
        d[c].append(e)

print(''.join([d[k][-1] for k in sorted(d.keys())]))
