from helper import *
from z3 import *

data = raw_data(2023, 24)
lines = lines(data)
HS = []
for line in lines:
    HS.append(tuple(map(int, re.findall(r'[+-]?\d+', line))))

x, y, z, dx, dy, dz = Int('x'), Int('y'), Int('z'), Int('dx'), Int('dy'), Int('dz')

T = [Int(f'T{i}') for i in range(len(HS))]
S = Solver()
for i in range(len(HS)):
    S.add(x + T[i] * dx - HS[i][0] - T[i] * HS[i][3] == 0)
    S.add(y + T[i] * dy - HS[i][1] - T[i] * HS[i][4] == 0)
    S.add(z + T[i] * dz - HS[i][2] - T[i] * HS[i][5] == 0)
S.check()
print(S.model().eval(x + y + z))
