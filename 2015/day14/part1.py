import re
import sys

t = 0
for line in sys.stdin.readlines():
    line = line.strip()
    s, d, r = map(int, re.findall(r'\d+', line))
    t = max(t, (2503 // (d + r) * d + min(d, 2503 % (d + r))) * s)

print(t)
