import itertools
from collections import deque


def p1(data: str):
    seq = deque()
    for n in map(int, data.splitlines()):
        if len(seq) < 25:
            seq.append(n)
        else:
            if not any(a + b == n for a, b in itertools.combinations(seq, 2)):
                return n
            seq.append(n)
            seq.popleft()


def p2(data: str):
    target = p1(data)
    ns = list(map(int, data.splitlines()))
    ns = ns[:ns.index(target)]
    for i in range(len(ns)):
        for j in range(1, len(ns) - i):
            if sum(ns[i:i + j + 1]) == target:
                ans = sorted(ns[i:i + 1 + j])
                return ans[0]+ans[-1]
