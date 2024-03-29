import re
from collections import deque


def solve(data: str, keep_order: bool):
    gi, si = data.split('\n\n')
    qs = [deque()]

    for line in [row[::-1] for row in zip(*gi.splitlines())]:
        q = deque()
        for c in line:
            if c.isalpha():
                q.append(c)
        if q:
            qs.append(q)
    for move in si.splitlines():
        c, f, t = list(map(int, re.findall(r'\d+', move)))
        if keep_order:
            qs[f].rotate(c)
        for _ in range(c):
            if keep_order:
                qs[t].append(qs[f].popleft())
            else:
                qs[t].append(qs[f].pop())
    return ''.join(qs[i][-1] for i in range(1, len(qs)))


def p1(data: str):
    return solve(data, False)


def p2(data: str):
    return solve(data, True)
