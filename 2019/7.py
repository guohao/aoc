import itertools
from collections import deque
from intcode import IntCodeVM


def p1(data: str):
    ans = 0
    for amps in itertools.permutations(list(range(5)), 5):
        cur_input = 0
        for amp in amps:
            vm = IntCodeVM(data)
            vm.rq.append(amp)
            vm.rq.append(cur_input)
            vm.run()
            cur_input = vm.sq.popleft()
        ans = max(ans, cur_input)
    return ans


def run_amps(amps: tuple, data: str):
    qs = [deque([amps[i]]) for i in range(5)]
    vms = [IntCodeVM(data, qs[i], qs[(i + 1) % 5]) for i in range(5)]
    qs[0].append(0)
    while True:
        for vm in vms:
            vm.run()
        if any(vm.halt for vm in vms):
            break
    return qs[0][-1]


def p2(data: str):
    ans = 0
    for amps in itertools.permutations(list(range(5, 10)), 5):
        ans = max(ans, run_amps(amps, data))
    return ans
