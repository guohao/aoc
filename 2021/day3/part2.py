import sys
from collections import Counter

lines = [line.strip() for line in sys.stdin.readlines()]

obc = lines
co2bc = lines
for i in range(len(lines[0])):
    if len(obc) != 1:
        c = Counter(x[i] for x in obc)
        mo = '1' if c['1'] >= c['0'] else '0'
        obc = [y for y in obc if y[i] == mo]
    if len(co2bc) != 1:
        c = Counter(x[i] for x in co2bc)
        mo = '0' if c['1'] >= c['0'] else '1'
        co2bc = [y for y in co2bc if y[i] == mo]

print(int(obc[0], 2) * int(co2bc[0], 2))
