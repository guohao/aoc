import itertools
from collections import defaultdict


def solve(data: str, add_me=False):
    ans = 0
    ps = set()
    pairs = defaultdict(int)
    for line in data.splitlines():
        cells = line.split()
        hc = int(cells[3])
        if cells[2] == 'lose':
            hc = -hc
        pairs[cells[0], cells[-1][:-1]] = hc
        ps.add(cells[0])
    ps = list(ps)
    if add_me:
        ps.append('_')
    for p in itertools.permutations(range(len(ps)), len(ps)):
        total_h = 0
        for i in range(len(p)):
            a = ps[p[i]]
            b = ps[p[(i + 1) % len(ps)]]
            c = ps[p[(i - 1) % len(ps)]]
            total_h += pairs[a, b]
            total_h += pairs[a, c]
        ans = max(total_h, ans)
    return ans


def p1(data: str):
    return solve(data)


def p2(data: str):
    return solve(data, True)
