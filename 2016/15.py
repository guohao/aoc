import itertools
import re


def solve(data: str, extra: bool):
    dists = []
    for line in data.splitlines():
        _, tp, _, ip = list(map(int, re.findall(r'\d+', line)))
        dists.append((tp, ip))
    if extra:
        dists.append((11, 0))
    for t in itertools.count(0):
        if all((dists[i][1] + t + i + 1) % dists[i][0] == 0 for i in range(len(dists))):
            return t


def p1(data: str):
    return solve(data, False)


def p2(data: str):
    return solve(data, True)
