import math
import sys
from collections import deque
from functools import reduce

pc = [0, 0]
dest = {}
types = {}
states = {}
ls = [l.strip() for l in sys.stdin.readlines()]
for line in ls:
    f, t = line.split(' -> ')
    name = f if f[0] not in '%&' else f[1:]
    dest[name] = t.split(', ')

    if f[0] == '%':
        types[name] = '%'
        states[name] = 0
    elif f[0] == '&':
        types[name] = '&'
        states[name] = {}
    else:
        types[name] = name
for m, tos in dest.items():
    for t in tos:
        if t in types and types[t] == '&':
            states[t][m] = 0
q = deque()


def send(name, pulse):
    for to in dest[name]:
        q.append((name, to, pulse))


needs = {'sg', 'dh', 'db', 'lm'}
cycles = {x: 0 for x in needs}
source = 'jm'
for i in range(10000):
    q.append(('', 'broadcaster', 0))
    while q:
        prev, curr, p = q.popleft()
        pc[p] += 1
        if p and prev in cycles.keys() and curr == source and not cycles[prev]:
            cycles[prev] = i + 1
            if all(cycles.values()):
                print(reduce(math.lcm, cycles.values()))
                exit()
        if curr not in types:
            continue
        match types[curr]:
            case 'broadcaster':
                send(curr, p)
            case '%':
                if p == 0:
                    states[curr] = 1 - states[curr]
                    send(curr, states[curr])
            case '&':
                states[curr][prev] = p
                send(curr, not all(states[curr].values()))
