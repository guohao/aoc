from collections import deque

import sys

from intcode import IntCodeVM

data = sys.stdin.read().strip()

q = deque([[]])
seen = set()
D = {1: (0, -1), 2: (0, 1), 3: (-1, 0), 4: (1, 0)}
while q:
    path = q.popleft()
    vm = IntCodeVM(data)
    x, y = 0, 0
    for move in path:
        vm.rq.append(move)
        vm.run()
        s = vm.sq.popleft()
        if s == 2:
            print(len(path))
            exit()
        elif s == 1:
            d = D[move]
            x, y = x + d[0], y + d[1]
    if (x, y) in seen:
        continue
    seen.add((x, y))
    for i in range(1, 5):
        q.append(path + [i])

