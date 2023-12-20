import re as regex
from collections import defaultdict

from helper import *

# 525181
# 84289137
data = raw_data(2023, 3)

data = """
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
"""
data = data.strip()
lines = lines(data)

ans = 0
for i, line in enumerate(lines):
    for m in regex.finditer(r'\d+', line):
        for x, y in itertools.product(range(i - 1, i + 2), range(m.start() - 1, m.end() + 1)):
            if not (0 <= x < len(lines[0]) and 0 <= y < len(lines)):
                continue
            if lines[x][y] != '.' and not lines[x][y].isdigit():
                ans += int(m.group())
                break
print(ans)

g = grid_2d(lines)
ans = 0
not_dot = set(x[1] for x in g.items() if not x[1].isdigit() and x[1] != '.')
print(not_dot)

points = [item for c in not_dot for item in g.findall(c)]
for p in points:
    move = p.moves(diagonals=True)
    ns = [n for n in p.neighbors(move) if g[n].isdigit()]
    if len(ns) ==2:
# print(points)
for line in lines:
    d = defaultdict(lambda: [])
    for i, line in enumerate(lines):
        for m in regex.finditer(r'\d+', line):
            for x, y in itertools.product(range(i - 1, i + 2), range(m.start() - 1, m.end() + 1)):
                if not (0 <= x < len(lines[0]) and 0 <= y < len(lines)):
                    continue
                if lines[x][y] != '.' and not lines[x][y].isdigit():
                    d[(x, y)].append(int(m.group()))
                    break
    ans += sum(v[0] * v[1] for v in d.values() if len(v) == 2)

print(ans)
