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
                print(y)
                exit()
            else:
                vms[a].rq.append(x)
                vms[a].rq.append(y)

