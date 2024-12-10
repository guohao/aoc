import re
import sys


def d(a, b) -> int:
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


lines = [l.strip() for l in sys.stdin.readlines()]
BS = {}
for line in lines:
    x1, y1, x2, y2 = list(map(int, re.findall(r'-?\d+', line)))
    BS[(x1, y1)] = (x2, y2)


def check(p) -> bool:
    for s, b in BS.items():
        if d(p, s) <= d(s, b):
            return True
    return False


ret = set()
for a, b in BS.items():
    diff = d(a, b) - abs(a[1] - 2000000)
    for i in range(a[0] - diff, a[0] + diff + 1):
        ret.add(i)

for b in BS.values():
    if b[1] == 2000000 and b[0] in ret:
        ret.remove(b[0])
print(len(ret))
