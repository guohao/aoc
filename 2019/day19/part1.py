from intcode import IntCodeVM


def state_of(data: str, x, y):
    vm = IntCodeVM(data)
    assert not vm.sq
    assert not vm.rq
    vm.rq.append(x)
    vm.rq.append(y)
    vm.run()
    return vm.sq.popleft()


import sys

data = sys.stdin.read().strip()

ans = 0
for x in range(50):
    for y in range(50):
        ans += state_of(data, x, y)
print(ans)

