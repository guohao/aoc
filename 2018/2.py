import itertools
from collections import Counter


def p1(data: str):
    n2 = 0
    n3 = 0
    for line in data.splitlines():
        c = Counter(line)
        if 2 in c.values():
            n2 += 1
        if 3 in c.values():
            n3 += 1
    return n2 * n3


def p2(data: str):
    ids = data.splitlines()
    for a, b in itertools.product(ids, repeat=2):
        if a == b:
            continue
        comm = [a[i] for i in range(len(a)) if a[i] == b[i]]
        if len(comm) == len(a) - 1:
            return ''.join(comm)
