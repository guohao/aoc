from helper import *

data = raw_data(2023, 24)
lines = lines(data)
HS = []
for line in lines:
    x, y, _, dx, dy, _ = map(int, re.findall('[+-]?\d+', line))
    # xt = x0 + t*dx
    # yt = y0 + t*dy
    # x0+ t*dx0 = x1 + t*dx1
    # y0 + t*dy0 = y1 + t*dy1
    HS.append((x, y, dx, dy))

ans = 0
MIN = 200000000000000
MAX = 400000000000000
for i in range(len(HS)):
    for j in range(i):
        a = HS[i]
        b = HS[j]
        ax, ay, adx, ady = a
        bx, by, bdx, bdy = b
        # x0 = adx * ta + ax
        # y0 = ady * ta + ay
        # x1 = bdx * tb + bx
        # y1 = bdy * tb + by
        # x0 = x1
        # adx * ta + ax =  bdx * tb + bx
        # ady * ta + ay  = bdy * tb + by
        # ta =(bdx * tb + bx -ax )/ adx
        # ady * (bdx * tb + bx -ax )/ adx + ay = bdy * tb + by
        # ady * bdx * tb + ady*(bx-ax) = adx*bdy *tb + adx*by - adx*ay
        # (ady * bdx -adx*bdy )*tb = adx*(by-ay) - ady*(bx-ax))
        # tb = (adx*by + ady*ax - ady*bx) / (ady * bdx - adx * bdy)
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
