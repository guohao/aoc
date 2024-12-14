import sys

parts = sys.stdin.read().split('\n\n')
ns = list(map(int, parts[0].split(',')))
gs = []
for part in parts[1:]:
    g = {}
    gv = {}
    for i, line in enumerate(part.splitlines()):
        for j, c in enumerate(line.split()):
            g[int(c)] = i, j
            gv[i, j] = int(c)
    gs.append((g, gv, set()))
wins = []
for n in ns:
    ngs = []
    for i in range(len(gs)):
        g, gv, v = gs[i]
        if n not in g:
            ngs.append((g, gv, v))
            continue
        x, y = g[n]
        v.add(n)
        r = range(int(len(g) ** 0.5))
        if all(gv[x, j] in v for j in r):
            wins.append((sum(g) - sum(v)) * n)
            continue
        if all(gv[j, y] in v for j in r):
            wins.append((sum(g) - sum(v)) * n)
            continue
        ngs.append((g, gv, v))
    gs = ngs
print(wins[-1])
