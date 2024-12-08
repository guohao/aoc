import re
import sys

ss = []
for line in sys.stdin.readlines():
    ss.append(list(map(int, re.findall(r'-?\d+', line))))
ans = 0
MIN = 200000000000000
MAX = 400000000000000
for i in range(len(ss)):
    for j in range(i):
        a = ss[i]
        b = ss[j]
        ax, ay, _, adx, ady, _ = a
        bx, by, _, bdx, bdy, _ = b
        if ady * bdx == adx * bdy:
            continue
        tb = (adx * (by - ay) - ady * (bx - ax)) / (ady * bdx - adx * bdy)
        if tb <= 0:
            continue
        ta = (bdx * tb + bx - ax) / adx
        if ta <= 0:
            continue
        xc = tb * bdx + bx
        yc = tb * bdy + by
        if MIN <= xc <= MAX and MIN <= yc <= MAX:
            ans += 1
print(ans)
