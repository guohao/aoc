import sys
import re

lines = [line.strip() for line in sys.stdin.readlines()]
t = 0
for line in lines:
    d, r = list(map(int, re.findall(r'-?\d+', line)))
    if d % (2 * r - 2) == 0:
        t += d * r
print(t)
