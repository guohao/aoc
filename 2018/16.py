import re
from collections import defaultdict

op_all = {
    'addr': lambda r, a, b: r[a] + r[b],
    'addi': lambda r, a, b: r[a] + b,
    'mulr': lambda r, a, b: r[a] * r[b],
    'muli': lambda r, a, b: r[a] * b,
    'banr': lambda r, a, b: r[a] & r[b],
    'bani': lambda r, a, b: r[a] & b,
    'borr': lambda r, a, b: r[a] | r[b],
    'bori': lambda r, a, b: r[a] | b,
    'setr': lambda r, a, _: r[a],
    'seti': lambda r, a, _: a,
    'gtir': lambda r, a, b: int(a > r[b]),
    'gtri': lambda r, a, b: int(r[a] > b),
    'gtrr': lambda r, a, b: int(r[a] > r[b]),
    'eqir': lambda r, a, b: int(a == r[b]),
    'eqri': lambda r, a, b: int(r[a] == b),
    'eqrr': lambda r, a, b: int(r[a] == r[b])}


def ints(line):
    return list(map(int, re.findall(r'-?\d+', line)))


def opcs(before, op, after):
    ret = set()
    for name, action in op_all.items():
        curr = before.copy()
        curr[op[3]] = action(curr, op[1], op[2])
        if curr == after:
            ret.add(name)
    return ret


def p1(data: str):
    ans = 0
    for part in data.split('\n\n\n')[0].split('\n\n'):
        if len(opcs(*list(map(ints, part.splitlines())))) > 2:
            ans += 1
    return ans


def p2(data: str):
    sample, test = data.split('\n\n\n')
    opm = defaultdict(lambda: set(op_all.keys()))
    for part in sample.split('\n\n'):
        before, ops, after = list(map(ints, part.splitlines()))
        opm[ops[0]] = opm[ops[0]].intersection(opcs(before, ops, after))
    nto = {}
    while len(nto) != len(opm):
        for k in opm:
            for found in nto.values():
                if found in opm[k]:
                    opm[k].remove(found)
            if len(opm[k]) == 1:
                nto[k] = list(opm[k])[0]
    assert len(nto) == 16

    r = [0] * 4
    for part in test.splitlines():
        if not part:
            continue
        op = ints(part)
        r[op[3]] = op_all[nto[op[0]]](r, op[1], op[2])
    return r[0]
