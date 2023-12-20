from collections import deque

from helper import *

data = raw_data(2023, 20)
lines = lines(data)
R = {}
C = {}
B = []
for line in lines:
    cells = line.split('->')
    if cells[0].startswith("bro"):
        B = [x.strip() for x in cells[1].split(',')]
    elif cells[0].startswith('%'):
        R[cells[0][1:].strip()] = [0, [x.strip() for x in cells[1].split(',')]]
    else:
        name = cells[0][1:].strip()
        C[name] = [{}, [x.strip() for x in cells[1].split(',')]]

for name, v in C.items():
    for r in R.items():
        if name in r[1][1]:
            C[name][0][r[0]] = 0
    for c in C.items():
        if name in c[1][1]:
            C[name][0][c[0]] = 0

needs = set()

source = ''


def dfs(name, depth):
    global source
    if depth == 0:
        return
    if depth == 1:
        needs.add(name)
        return
    for r in R.items():
        if name in r[1][1]:
            source = name
            dfs(r[0], depth - 1)
    for c in C.items():
        if name in c[1][1]:
            source = name
            dfs(c[0], depth - 1)


dfs('rx', 3)
cycles = {x: 0 for x in needs}
dq = deque()
cnts = [0, 0]
stop = False
for i in range(100000):
    if i == 1000:
        print(cnts[0] * cnts[1])

    dq.append(('button', 'broadcaster', 0))
    if stop:
        break
    while dq:
        s, d, p = dq.popleft()
        if p:
            if s in cycles.keys() and d == source and not cycles[s]:
                cycles[s] = i + 1
                if all(cycles.values()):
                    x = 1
                    for c in cycles.values():
                        x = lcm(c, x)
                    print(x)
                    stop = True
        if d == 'rx' and p == 0:
            stop = True
        cnts[p] += 1
        if d in R.keys():
            if p:
                continue
            R[d][0] = 1 - R[d][0]
            for x in R[d][1]:
                dq.append((d, x, R[d][0]))
        elif d in C.keys():
            C[d][0][s] = p
            for x in C[d][1]:
                dq.append((d, x, not all(C[d][0].values())))
        elif d == 'broadcaster':
            for x in B:
                dq.append((d, x, 0))
