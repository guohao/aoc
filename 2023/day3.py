import re as regex
from collections import defaultdict

import helper

data = io_utils.get_data(2023, 3)
lines = io_utils.raw_str_to_lines(data)

ans1 = 0
d = defaultdict(list)
for i, line in enumerate(lines):
    for m in regex.finditer(r'\d+', line):
        x = [x for x in range(i - 1, i + 2)]
        y = [y for y in range(m.start() - 1, m.end() + 1)]
        idx = [(a, b) for a in x for b in y]
        count = sum(0 <= a < len(lines) and 0 <= b < len(line) and lines[a][b] != '.'
                    and not (a == i and m.start() <= b < m.end())
                    for a, b in idx)
        if count > 0:
            ans1 += int(m.group())
    for m in regex.finditer(r'\d+', line):
        x = [x for x in range(i - 1, i + 2)]
        y = [y for y in range(m.start() - 1, m.end() + 1)]
        idx = [(a, b) for a in x for b in y]
        stars = [(a, b) for a, b in idx if
                 0 <= a < len(lines) and 0 <= b < len(line) and lines[a][b] == '*' and not (
                         a == i and m.start() <= b < m.end())]
        for s in stars:
            d[s].append((int(m.group())))
ans2 = sum(v[0] * v[1] for v in d.values() if len(v) == 2)
print(ans1)
print(ans2)
