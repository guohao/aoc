import re


def ints(line):
    return list(map(int, re.findall(r'-?\d+', line)))


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


def calc(r5, r4):
    while True:
        r5 = (((r5 + (r4 & 255)) & 16777215) * 65899) & 16777215
        if r4 < 256:
            return r5
        r4 = r4 // 256


def p1(data: str):
    r4 = 65536
    r5 = 13431073
    return calc(r5, r4)


def p2(data: str):
    seen = []
    r5 = 0
    while True:
        r4 = r5 | 65536
        r5 = 13431073
        r5 = calc(r5, r4)
        if r5 in seen:
            return seen[-1]
        seen.append(r5)
