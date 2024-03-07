def p1(data: str):
    cmps = []
    for line in data.splitlines():
        a, b = map(int, line.split('/'))
        cmps.append((a, b))
    cmps = set(cmps)

    def dfs(visited: tuple, pn=None):
        ans = 0
        for c in cmps - set(visited):
            if pn not in c:
                continue
            npn = c[0] if c[1] == pn else c[1]
            ans = max(ans, sum(c) + dfs(visited + (c,), npn))
        return ans

    return dfs((), 0)


def p2(data: str):
    cmps = []
    for line in data.splitlines():
        a, b = map(int, line.split('/'))
        cmps.append((a, b))
    cmps = set(cmps)

    def dfs(visited: tuple, pn=None):
        length, strength = 0, 0
        for c in cmps - set(visited):
            if pn not in c:
                continue
            npn = c[0] if c[1] == pn else c[1]
            nl, ns = dfs(visited + (c,), npn)
            nl += 1
            ns += sum(c)
            if nl > length:
                length = nl
                strength = ns
            elif nl == length:
                strength = max(ns, strength)
        return length, strength

    return dfs((), 0)[1]
