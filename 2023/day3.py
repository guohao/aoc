import itertools
import re as regex
from collections import defaultdict

from helper import *


# 525181
# 84289137

def f(lines):
    ret = 0
    for i, line in enumerate(lines):
        for m in regex.finditer(r'\d+', line):
            for x, y in itertools.product(range(i - 1, i + 2), range(m.start() - 1, m.end() + 1)):
                if not (0 <= x < len(lines[0]) and 0 <= y < len(lines)):
                    continue
                if lines[x][y] != '.' and not lines[x][y].isdigit():
                    ret += int(m.group())
                    break
    return ret


def f2(lines):
    d = defaultdict(lambda: [])
    for i, line in enumerate(lines):
        for m in regex.finditer(r'\d+', line):
            for x, y in itertools.product(range(i - 1, i + 2), range(m.start() - 1, m.end() + 1)):
                if not (0 <= x < len(lines[0]) and 0 <= y < len(lines)):
                    continue
                if lines[x][y] != '.' and not lines[x][y].isdigit():
                    d[(x, y)].append(int(m.group()))
                    break
    return sum(v[0] * v[1] for v in d.values() if len(v) == 2)


p = Puzzle(2023, 3)
p.solve_lines(f)
p.solve_lines(f2)
