import re
import sys
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

parts = sys.stdin.read().split('\n\n\n\n')
opd = defaultdict(set)

for p in parts[0].split('\n\n'):
    b, c, a = [list(map(int, re.findall(r'-?\d+', l))) for l in p.splitlines()]
    for name, op in op_all.items():
        r = b.copy()
        r[c[3]] = op(r, c[1], c[2])
        if r == a:
            opd[c[0]].add(name)

while True:
    if all(len(v) == 1 for v in opd.values()):
        opd = {k: list(v)[0] for k, v in opd.items()}
        break
    for k, v in opd.copy().items():
        if len(v) == 1:
            vv = list(v)[0]
            for k2, v2 in opd.items():
                if k2 == k:
                    continue
                if vv in v2:
                    v2.remove(vv)

R = defaultdict(int)
for line in parts[1].splitlines():
    line = line.strip()
    c = list(map(int, re.findall(r'-?\d+', line)))
    op = op_all[opd[c[0]]]
    R[c[3]] = op(R, c[1], c[2])
print(R[0])
