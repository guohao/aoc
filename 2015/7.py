import re
from collections import deque


def solve(data: str, b: int):
    r = {}
    q = deque(data.splitlines())

    def value_of(k: str):
        if re.fullmatch(r'-?\d+', k):
            return int(k)
        return r[k]

    def has_value(k):
        return re.fullmatch(r'-?\d+', k) or k in r

    while q:
        line = q.popleft()
        op, t = line.split(' -> ')
        if t == 'b' and b:
            r[t] = b
            continue
        cells = op.split()
        if any(not has_value(v) for v in cells if v.islower()):
            q.append(line)
            continue

        if len(cells) == 1:
            r[t] = value_of(cells[0])
        elif cells[0] == 'NOT':
            r[t] = ~ r[cells[1]]
        elif len(cells) == 3:
            a, b, c = cells
            a = value_of(a)
            c = value_of(c)
            if b == 'AND':
                r[t] = a & c
            elif b == 'OR':
                r[t] = a | c
            elif b == 'LSHIFT':
                r[t] = a << c
            elif b == 'RSHIFT':
                r[t] = a >> c
    return r['a']


def p1(data: str):
    return solve(data, 0)


def p2(data: str):
    return solve(data, solve(data, 0))
