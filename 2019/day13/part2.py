import intcode

import sys

data = sys.stdin.read().strip()

data = '2' + data[1:]
vm = intcode.IntCodeVM(data)
sq = vm.sq
rq = vm.rq
score = 0
paddle_x = 0
while True:
    vm.run()
    if not sq:
        break
    x = sq.popleft()
    y = sq.popleft()
    t = sq.popleft()
    if (x, y) == (-1, 0):
        score = t
        continue
    if t == 3:
        paddle_x = x
    elif t == 4:
        rq.append(int((x > paddle_x) - (x < paddle_x)))

print(score)
