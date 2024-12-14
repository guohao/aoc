import sys
from copy import deepcopy as dc


data = sys.stdin.read().strip()

def rotations(s):
    s = dc(s)
    k = []
    for _ in range(4):
        for _ in range(4):
            k.append(s)
            s = {(z, y, -x) for x, y, z in s}
        k.append({(y, -x, z) for x, y, z in s})
        k.append({(-y, x, z) for x, y, z in s})
        s = {(x, z, -y) for x, y, z in s}
    return k


def vsub(x, y):
    return tuple(a - b for a, b in zip(x, y))


scanners = []

for s in data.split("\n\n"):
    s = s.splitlines()[1:]
    scanners.append({tuple(map(int, k.split(","))) for k in s})

t = set(scanners[0])

q = scanners[1:]

def calc_intersect(s1, s2):
    for s2 in rotations(s2):
        for a in s1:
            for b in s2:
                off = vsub(b, a)
                c = {vsub(b, off) for b in s2}
                if len(s1 & c) >= 12:
                    return c

while q:
    k = calc_intersect(t, q[0])
    if k:
        t |= k
        q.pop(0)
    else:
        q.append(q.pop(0))

print(len(t))


def p2(data: str):
    scanners = []

    for s in data.split("\n\n"):
        s = s.splitlines()[1:]
        scanners.append({tuple(map(int, k.split(","))) for k in s})

