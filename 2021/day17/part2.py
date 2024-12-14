import re
import sys

data = sys.stdin.read().strip()

xl, xr, yd, yu = list(map(int, re.findall(r'-?\d+', data.strip())))


def can_within(vx, vy):
    sx, sy = 0, 0
    maxy = 0
    while sy >= yd:
        sx, sy = sx + vx, sy + vy
        maxy = max(maxy, sy)
        if xl <= sx <= xr and yd <= sy <= yu:
            return maxy
        if vx > 0:
            vx -= 1
        elif vx < 0:
            vx += 1
        vy -= 1
    return -1


ans = set()
for i in range(1, xr + 1):
    for j in range(-xr, xr + 1):
        my = can_within(i, j)
        if my != -1:
            ans.add((i, j))
print(len(ans))
