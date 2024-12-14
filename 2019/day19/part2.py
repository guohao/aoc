from intcode import IntCodeVM


def state_of(data: str, x, y):
    vm = IntCodeVM(data)
    assert not vm.sq
    assert not vm.rq
    vm.rq.append(x)
    vm.rq.append(y)
    vm.run()
    return vm.sq.popleft()


def match(data, x, y):
    ur = state_of(data, x + 99, y)
    ul = state_of(data, x, y)
    dl = state_of(data, x, y + 99)
    dr = state_of(data, x, y + 99)
    return ur and ul and dr and dl


import sys

data = sys.stdin.read().strip()


def s(xs, y):
    for i in range(xs, 10000):
        if state_of(data, i, y):
            return i
    return xs


def e(xs, y):
    for i in range(xs, 10000):
        if not state_of(data, i, y):
            return i - 1
    return xs


l = 0
for y in range(1200, 1300):
    l = s(l, y)
    r = e(l, y)
    if match(data, r - 99, y):
        print((r - 99) * 10000 + y)
        break
