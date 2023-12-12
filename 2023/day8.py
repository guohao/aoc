import itertools
import math
import re
from functools import reduce

import helper

data = helper.raw_data(2023, 8)
lines = helper.lines(data)
cmds = cycle_iterator = itertools.cycle([1 if 'R' == x else 0 for x in re.findall(r'\w', lines[0])])
pos = {}
for line in lines[1:]:
    a, b, c = re.findall(r'\w+', line)
    pos[a] = (b, c)

ps = 'AAA'
for t, cmd in enumerate(cmds, start=1):
    ps = pos[ps][cmd]
    if ps == 'ZZZ':
        print(t)
        break

ps = [x for x in pos.keys() if x.endswith('A')]

fc = [0] * len(ps)
for t, cmd in enumerate(cmds, start=1):
    if sum(x > 0 for x in fc) == len(ps):
        break
    for i, p in enumerate(ps):
        if fc[i] > 0:
            continue
        ps[i] = pos[p][cmd]
        if ps[i].endswith("Z"):
            fc[i] = t


def lcm(a: int, b: int) -> int:
    return a * b // math.gcd(a, b)


print(reduce(lcm, fc))
