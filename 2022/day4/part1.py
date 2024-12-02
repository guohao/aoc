import re
import sys

ls = [line.strip() for line in sys.stdin.readlines()]
t = 0
for line in ls:
    a, b, c, d = list(map(int, re.findall(r'\d+', line)))
    t += (c - a) * (d - b) <= 0
print(t)
