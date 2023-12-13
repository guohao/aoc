from collections import defaultdict

from helper import *


def f(i, line):
    if not re.findall(r'((1[3-9]|[2-9]\d) red)|((1[5-9]|[2-9]\d) blue)|((1[4-9]|[2-9]\d) green)', line):
        return i + 1
    return 0


def f2(line):
    d = defaultdict(lambda: 0)
    for m in re.finditer(r'\d+\s+(blue|green|red)', line):
        count, color = m.group().split(' ')
        d[color] = max(int(count), d[color])
    return reduce(lambda a, b: a * b, d.values())


p = Puzzle(2023, 2)
p.solve_eline(f)
p.solve_line(f2)
