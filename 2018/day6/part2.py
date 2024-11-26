import itertools
import re
import sys

ps = []
for line in sys.stdin.readlines():
    line = line.strip()
    digits = tuple(map(int, re.findall(r'-?\d+', line)))
    ps.append(digits)
minX = min(x[0] for x in ps)
minY = min(x[1] for x in ps)
maxX = max(x[0] for x in ps)
maxY = max(x[1] for x in ps)

t = 0
for i, j in itertools.product(range(minX, maxX + 1), range(minY, maxY + 1)):
    t += sum((abs(k[0] - i) + abs(k[1] - j)) for k in ps) < 10000

print(t)
