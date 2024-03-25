import math
from collections import Counter, defaultdict


def extract_triple(s: str) -> tuple[int, int, int]:
    s = s[3:-1]
    return tuple(map(int, s.split(',')))


def p1(data: str):
    ps = []
    for i, line in enumerate(data.splitlines()):
        p, v, a = map(extract_triple, line.split(', '))
        ps.append((i, p, v, a))
    c = Counter()
    for _ in range(1000):
        nps = []
        closest_p = math.inf
        closest_i = math.inf
        for particle in ps:
            i, p, v, a = particle
            v = tuple(v[i] + a[i] for i in range(3))
            p = tuple(p[i] + v[i] for i in range(3))
            nps.append((i, p, v, a))
            md = sum(abs(x) for x in p)
            if closest_p > md:
                closest_p = md
                closest_i = i
        ps = nps
        c[closest_i] += 1
    return c.most_common(1)[0][0]


def p2(data: str):
    ps = []
    for i, line in enumerate(data.splitlines()):
        p, v, a = map(extract_triple, line.split(', '))
        ps.append((i, p, v, a))
    for _ in range(1000):
        nps = []
        dp = defaultdict(list)
        for particle in ps:
            i, p, v, a = particle
            v = tuple(v[i] + a[i] for i in range(3))
            p = tuple(p[i] + v[i] for i in range(3))
            nps.append((i, p, v, a))
            dp[p].append(i)
        for collides in dp.values():
            if len(collides) > 1:
                for i in collides:
                    nps = list(filter(lambda x: x[0] != i, nps))
        ps = nps
    return len(ps)
