from util import *


def p1(data: str):
    parts = d2p(data)
    ins = itertools.cycle(parts[0])
    d = {}
    for line in parts[1].splitlines():
        f, l, r = re.findall(r'\w{3}', line)
        d[f] = {'L': l, 'R': r}
    node = 'AAA'
    for t in itertools.count():
        if node == 'ZZZ':
            return t
        node = d[node][next(ins)]


def p2(data: str):
    parts = d2p(data)
    ins = itertools.cycle(parts[0])
    d = {}
    for line in parts[1].splitlines():
        f, l, r = re.findall(r'\w{3}', line)
        d[f] = {'L': l, 'R': r}
    cycles = []
    for node in [x for x in d.keys() if x[-1] == 'A']:
        for t in itertools.count():
            if node[-1] == 'Z':
                cycles.append(t)
                break
            node = d[node][next(ins)]
    return lcm(cycles)
