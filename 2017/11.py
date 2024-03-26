from collections import Counter


def p1(data: str):
    c = Counter(data.strip().split(','))
    pairs = [('sw', 'ne'), ('se', 'nw'), ('s', 'n')]
    print(c)
    for pair in pairs:
        c[pair[0]] -= c[pair[1]]
        c[pair[1]] = 0
    c['se'] -= c['sw']
    c['s'] += c['sw']
    c['sw'] = 0
    print(c)
    return sum(c.values())


def p2(data: str):
    c = Counter()
    pairs = [('sw', 'ne'), ('se', 'nw'), ('s', 'n')]
    ans = 0
    for ch in data.strip().split(','):
        c[ch] += 1
        for pair in pairs:
            c[pair[0]] -= c[pair[1]]
            c[pair[1]] = 0
        c['se'] -= c['sw']
        c['s'] += c['sw']
        c['sw'] = 0
        ans = max(ans, sum(c.values()))
    return ans
