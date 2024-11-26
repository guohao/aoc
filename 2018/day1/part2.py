import sys
from itertools import cycle

t = 0
seen = set()
for line in cycle(sys.stdin.readlines()):
    seen.add(t)
    t += int(line)
    if t in seen:
        print(t)
        exit()
