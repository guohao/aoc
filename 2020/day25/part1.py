import itertools

import sys

data = sys.stdin.read().strip()

cpk, dpk = list(map(int, data.splitlines()))


def loop_times(target):
    n = 1
    for t in itertools.count(1):
        n = (n * 7) % 20201227
        if n == target:
            return t


clt = loop_times(cpk)
n = 1
for _ in range(clt):
    n = (n * dpk) % 20201227
print(n)
