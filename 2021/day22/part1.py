import re
import sys

g = {}
data = sys.stdin.read().strip()

for line in data.splitlines():
    toggle = line.startswith('on')
    x0, x1, y0, y1, z0, z1 = list(map(int, re.findall(r'-?\d+', line)))
    x0 = max(-50, x0)
    x1 = min(50, x1)
    y0 = max(-50, y0)
    y1 = min(50, y1)
    z0 = max(-50, z0)
    z1 = min(50, z1)
    for ix in range(x0, x1 + 1):
        for iy in range(y0, y1 + 1):
            for iz in range(z0, z1 + 1):
                g[ix, iy, iz] = toggle
print(sum(g.values()))
