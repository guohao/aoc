import itertools


def solve(data: str):
    G = {}
    for i, line in enumerate(data.splitlines()):
        for j, c in enumerate(line):
            if len(c.strip()) > 0:
                G[(i, j)] = c
    start = (0, -1)
    for i in itertools.count():
        p = (0, i)
        if p in G and G[p] == '|':
            start = p
            break
    d = (1, 0)
    prev = (-1, -1)
    cur = start
    ans = ''
    ans2 = 0
    while True:
        ans2 += 1
        if G[cur].isalpha():
            ans += G[cur]
        if (cur[0] + d[0], cur[1] + d[1]) in G:
            prev = cur
            cur = (cur[0] + d[0], cur[1] + d[1])
            continue
        else:
            ds = {(1, 0), (-1, 0), (0, 1), (0, -1)} - {d}
            found = False
            for nd in ds:
                nb = (cur[0] + nd[0], cur[1] + nd[1])
                if nb == prev:
                    continue
                if nb in G:
                    prev = cur
                    cur = nb
                    d = nd
                    found = True
                    break
            if not found:
                break
    return ans, ans2


def p1(data: str):
    return solve(data)[0]


def p2(data: str):
    return solve(data)[1]
