import math
import re
import sys

lines = [line.strip() for line in sys.stdin.readlines()]
ps = []
for line in lines:
    ps.append(list(map(int, re.findall(r'-?\d+', line))))

ans = -1
for _ in range(1000):
    n = math.inf
    nid = -1
    for i in range(len(ps)):
        v = [ps[i][3 + j] + ps[i][6 + j] for j in range(3)]
        c = [ps[i][j] + ps[i][3 + j] for j in range(3)]
        ps[i] = c + v + ps[i][6:]
        dist = sum(abs(ps[i][j]) for j in range(3))
        if dist < n:
            n = dist
            nid = i
    ans = nid

print(ans)
