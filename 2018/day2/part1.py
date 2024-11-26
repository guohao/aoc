import sys
from collections import Counter

a = b = 0
for line in sys.stdin.readlines():
    line = line.strip()
    c = Counter(line)
    if 2 in c.values():
        a += 1
    if 3 in c.values():
        b += 1
print(a * b)
