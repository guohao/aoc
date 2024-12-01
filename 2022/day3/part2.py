import sys
from functools import reduce

lines = [line.strip() for line in sys.stdin.readlines()]
t = 0
for i in range(0, len(lines), 3):
    tg = lines[i:i + 3]
    c = list(reduce(lambda x, y: x & y, map(set, tg)))[0]
    t += ord(c) + 1
    if 'a' <= c <= 'z':
        t -= ord('a')
    else:
        t -= ord('A')
        t += 26
print(t)
