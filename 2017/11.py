from collections import Counter


def simplify(c):
    if c['n']:
        c['nw'] += c['n']
        c['ne'] += c['n']
        c['n'] = 0
    if c['s']:
        c['sw'] += c['s']
        c['se'] += c['s']
        c['s'] = 0
    while c['ne'] and c['sw']:
        c['ne'] -= 1
        c['sw'] -= 1
    while c['nw'] and c['se']:
        c['nw'] -= 1
        c['se'] -= 1
    while c['se'] and c['sw']:
        c['s'] += 1
        c['se'] -= 1
        c['sw'] -= 1
    while c['nw'] and c['ne']:
        c['n'] += 1
        c['nw'] -= 1
        c['ne'] -= 1
    return c


def p1(data: str):
    c = Counter()
    for p in data.strip().split(','):
        c[p] += 1
        c = simplify(c)
    return sum(c.values())


def p2(data: str):
    c = Counter()
    m = 0
    for p in data.strip().split(','):
        c[p] += 1
        c = simplify(c)
        m = max(m, sum(c.values()))
    return m
