from util import *
from z3 import *


def p1(data: str):
    ss = list(map(ints, data.splitlines()))
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
    return ans


def p2(data: str):
    ss = list(map(ints, data.splitlines()))

    x, y, z, dx, dy, dz = Int('x'), Int('y'), Int('z'), Int('dx'), Int('dy'), Int('dz')

    T = [Int(f'T{i}') for i in range(len(ss))]
    s = Solver()
    for i in range(len(ss)):
        s.add(x + T[i] * dx - ss[i][0] - T[i] * ss[i][3] == 0)
        s.add(y + T[i] * dy - ss[i][1] - T[i] * ss[i][4] == 0)
        s.add(z + T[i] * dz - ss[i][2] - T[i] * ss[i][5] == 0)
    s.check()
    return s.model().eval(x + y + z)
