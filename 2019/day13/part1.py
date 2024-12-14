import intcode

import sys

data = sys.stdin.read().strip()

vm = intcode.IntCodeVM(data)
vm.run()
sq = vm.sq
g = {}
while sq:
    x = sq.popleft()
    y = sq.popleft()
    t = sq.popleft()
    if t == 2:
        g[x, y] = t
print(len(g))

