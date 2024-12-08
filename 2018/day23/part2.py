import re
from z3 import *


def ints(line):
    return list(map(int, re.findall(r'-?\d+', line)))


def bots_of_input(data: str):
    bots = []
    for line in data.splitlines():
        x, y, z, r = ints(line)
        bots.append(((x, y, z), r))
    return bots


data = sys.stdin.read()
bots = bots_of_input(data)
max_r = max(bot[1] for bot in bots)
bot = [bot for bot in bots if bot[1] == max_r][0]

bots = bots_of_input(data)


def my_abs(x):
    return If(x >= 0, x, -x)


o = Optimize()
(x, y, z) = (Int('x'), Int('y'), Int('z'))
in_ranges = [
    Int('in_range_' + str(i)) for i in range(len(bots))
]
range_count = Int('sum')
for i in range(len(bots)):
    (nx, ny, nz), r = bots[i]
    o.add(in_ranges[i] == If(my_abs(x - nx) + my_abs(y - ny) + my_abs(z - nz) <= r, 1, 0))
o.add(range_count == sum(in_ranges))
dist_from_zero = Int('dist')
o.add(dist_from_zero == my_abs(x) + my_abs(y) + my_abs(z))
o.maximize(range_count)
h2 = o.minimize(dist_from_zero)
o.check()
print(o.lower(h2).as_long())
