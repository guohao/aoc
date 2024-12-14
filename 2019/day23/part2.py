import itertools
from collections import deque

from intcode import IntCodeVM

import sys

data = sys.stdin.read().strip()

n = 50
vms = []

for i in range(n):
    vm = IntCodeVM(data, deque(), deque())
    vm.rq.append(i)
    vms.append(vm)
nat = None
seen = set()
for _ in itertools.count():
    has_sq = False
    for i in range(n):
        vm = vms[i]
        if not vm.rq:
            vm.rq.append(-1)
        vm.run()
        while vm.sq:
            has_sq = True
            a = vm.sq.popleft()
            x = vm.sq.popleft()
            y = vm.sq.popleft()
            if a == 255:
                nat = x, y
            else:
                vms[a].rq.append(x)
                vms[a].rq.append(y)
    if not has_sq and nat:
        vms[0].rq.append(nat[0])
        if nat[1] in seen:
            print(nat[1])
            exit()
        seen.add(nat[1])
        vms[0].rq.append(nat[1])
