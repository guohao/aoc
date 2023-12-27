from helper import *
from z3 import *

data = raw_data(2023, 24)
lines = lines(data)
HS = []
for line in lines:
    x, y, z, dx, dy, dz = map(int, re.findall(r'[+-]?\d+', line))
    HS.append((x, y, z, dx, dy, dz))

ans = 0
MIN = 200000000000000
MAX = 400000000000000
for i in range(len(HS)):
    for j in range(i):
        a = HS[i]
        b = HS[j]
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

x, y, z, dx, dy, dz = Int('x'), Int('y'), Int('z'), Int('dx'), Int('dy'), Int('dz')

T = [Int(f'T{i}') for i in range(len(HS))]
S = Solver()
for i in range(len(HS)):
    S.add(x + T[i] * dx - HS[i][0] - T[i] * HS[i][3] == 0)
    S.add(y + T[i] * dy - HS[i][1] - T[i] * HS[i][4] == 0)
    S.add(z + T[i] * dz - HS[i][2] - T[i] * HS[i][5] == 0)
S.check()
print(S.model().eval(x + y + z))
