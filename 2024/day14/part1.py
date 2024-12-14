import itertools
import math
import re
import sys

X = 101
Y = 103
rs = []
for line in sys.stdin.readlines():
    p0, p1, v0, v1 = list(map(int, re.findall(r'-?\d+', line)))
    rs.append(((p0, p1), (v0, v1)))

for _ in range(100):
    ns = []
    for (x, y), (dx, dy) in rs:
        nx = (x + dx) % X
        ny = (y + dy) % Y
        ns.append(((nx, ny), (dx, dy)))
    rs = ns

ans = [0] * 4
MX = X // 2
MY = Y // 2
for (x, y), _ in rs:
    if x > MX and y > MY:
        ans[0] += 1
    elif x > MX and y < MY:
        ans[1] += 1
    elif x < MX and y > MY:
        ans[2] += 1
    elif x < MX and y < MY:
        ans[3] += 1

print(math.prod(ans))
