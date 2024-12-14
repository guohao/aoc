from collections import deque, defaultdict
from intcode import IntCodeVM

import sys

data = sys.stdin.read().strip()

vm = IntCodeVM(data)

g = defaultdict(int)
q = deque()
q.append(((0, 0), (0, 1), 0))
sq = vm.sq
rq = vm.rq
while q:
    (x, y), (dx, dy), c = q.popleft()
    rq.append(g[x, y])
    vm.run()
    if vm.halt:
        break
    g[x, y] = sq.popleft()
    if sq.popleft():
        dx, dy = dy, -dx
    else:
        dx, dy = -dy, dx
    x, y = x + dx, y + dy
    q.append(((x, y), (dx, dy), g[x, y]))
print(len(g))
