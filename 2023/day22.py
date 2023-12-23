from collections import defaultdict, deque

from helper import *

data = raw_data(2023, 22).strip()
bricks = []
lines = lines(data)
for line in lines:
    x0, y0, z0, x1, y1, z1 = nums(line)
    if z0 > z1:
        x0, y0, z0, x1, y1, z1 = x1, y1, z1, x0, y0, z0
    if x0 == x1:
        brick = [(x0, y) for y in range(min(y0, y1), max(y0, y1) + 1)]
    else:
        brick = [(x, y0) for x in range(min(x0, x1), max(x0, x1) + 1)]
    bricks.append((set(brick), (z0, z1)))

bricks.sort(key=lambda x: x[1][0])
supporting = defaultdict(list)
supported_by = defaultdict(list)
H = defaultdict(lambda: -1)
B2L = defaultdict(lambda: -1)
H2B = defaultdict(list)
for i, bt in enumerate(bricks):
    brick, z = bt
    zbase = 0
    for point in brick:
        zbase = max(H[point] + 1, zbase)
    B2L[i] = zbase
    for point in brick:
        H[point] = zbase + z[1] - z[0]
    H2B[zbase + z[1] - z[0]].append(i)

for i, bs in enumerate(bricks[1:]):
    for b in H2B[B2L[i + 1] - 1]:
        if bricks[b][0] & bs[0]:
            supporting[b].append(i + 1)
            supported_by[i + 1].append(b)

ans = 0
for s in supporting.values():
    ans += all(len(supported_by[b]) > 1 for b in s)
ans += len(bricks) - len(supporting)
print(ans)


def bfs(broke):
    dq = deque()
    dq.append(broke)
    v = set()
    v.add(broke)
    while dq:
        nb = dq.popleft()
        for bb in supporting[nb]:
            if all(sb in v for sb in supported_by[bb]):
                dq.append(bb)
                v.add(bb)
    return len(v) - 1


print(sum(bfs(b) for b in range(len(bricks))))
