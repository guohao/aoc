import itertools
from collections import deque
from intcode import IntCodeVM
import sys

data = sys.stdin.read().strip()


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


ans = 0
for amps in itertools.permutations(list(range(5, 10)), 5):
    ans = max(ans, run_amps(amps, data))
print(ans)
