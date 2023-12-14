import re
from collections import defaultdict

from helper import *


def f(line):
    line = line.split(":")[1]
    a, b = [list(map(extract_num, part.split())) for part in line.split("|")]
    c = count_intersect(a, b)
    if c == 0:
        return 0
    return 2 ** (c - 1)


def f2(lines):
    d = defaultdict(lambda: 1)
    d[0] = 1
    for i, line in enumerate(lines, start=1):
        line = line.split(":")[1].strip()
        a, b = [list(map(extract_num, part.split())) for part in line.split("|")]
        c = count_intersect(a, b)
        for j in range(i + 1, i + 1 + c):
            d[j] += d[i]

    return sum(d.values())


p = Puzzle(2023, 4)
p.solve_line(f)
p.solve_lines(f2)
