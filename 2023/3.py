import math
import re
from collections import defaultdict

import util


def p1(data: str):
    g = util.grid_of(data)
    g = {k: c for k, c in g.items() if c != '.' and not c.isdigit()}
    ans = 0
    for i, line in enumerate(data.splitlines()):
        for m in re.finditer(r'\d+', line):
            for j in range(m.start(), m.end()):
                if any(nb in g for nb in util.neighbors_2d_8(i, j)):
                    ans += int(m.group())
                    break
    return ans


def p2(data: str):
    g = util.grid_of(data)
    g = {k: c for k, c in g.items() if c != '.' and not c.isdigit()}
    gear = defaultdict(set)

    def handle():
        for m in re.finditer(r'\d+', line):
            for j in range(m.start(), m.end()):
                for nb in util.neighbors_2d_8(i, j):
                    if nb in g and g[nb] == '*':
                        gear[nb].add(int(m.group()))

    for i, line in enumerate(data.splitlines()):
        handle()

    return sum(math.prod(v) for v in gear.values() if len(v) == 2)
