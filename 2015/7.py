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
        if len(cells) == 1 and has_value(cells[0]):
            r[t] = value_of(cells[0])
        elif len(cells) == 2 and has_value(cells[1]):
            r[t] = ~ r[cells[1]]
        elif len(cells) == 3 and has_value(cells[0]) and has_value(cells[2]):
            a, b, c = cells
            if b == 'AND':
                r[t] = value_of(a) & value_of(c)
            elif b == 'OR':
                r[t] = value_of(a) | value_of(c)
            elif b == 'LSHIFT':
                r[t] = value_of(a) << value_of(c)
            elif b == 'RSHIFT':
                r[t] = value_of(a) >> value_of(c)
        else:
            q.append(line)
    return r['a']


def p1(data: str):
    return solve(data, 0)


def p2(data: str):
    return solve(data, solve(data, 0))
