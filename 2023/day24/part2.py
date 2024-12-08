import re
from z3 import *

ls = []
for line in sys.stdin.readlines():
    ls.append(list(map(int, re.findall(r'-?\d+', line))))
n = len(ls)
x, y, z, dx, dy, dz = Real('x'), Real('y'), Real('z'), Real('dx'), Real('dy'), Real('dz')

T = [Real(f'T{i}') for i in range(len(ls))]
s = Solver()
for i in range(len(ls)):
    s.add(x + T[i] * dx - ls[i][0] - T[i] * ls[i][3] == 0)
    s.add(y + T[i] * dy - ls[i][1] - T[i] * ls[i][4] == 0)
    s.add(z + T[i] * dz - ls[i][2] - T[i] * ls[i][5] == 0)
s.check()
print(s.model().eval(x + y + z))
