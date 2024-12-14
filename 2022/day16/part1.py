import functools
import re
import sys

lines = [l.strip() for l in sys.stdin.readlines()]

D = {}
for i, line in enumerate(lines):
    cells = line.split()
    r = list(map(int, re.findall(r'-?\d+', line)))[0]
    c, ov = cells[1],cells[9:]
    ov = [x.replace(',', '') for x in ov]
    D[c] = (r, ov)


@functools.cache
def dfs(current, ov: str, time_left) -> int:
    if time_left == 1:
        return 0
    time_left = time_left - 1
    if current in ov or D[current][0] == 0:
        return max(dfs(c, ov, time_left) for c in D[current][1])
    else:
        return time_left * D[current][0] + dfs(current, ov + ',' + current, time_left)


ret = dfs('AA', '', 30)
print(ret)
