import sys

ls = [l.strip() for l in sys.stdin.readlines()]
g = {(i, j): ls[i][j] for i in range(len(ls)) for j in range(len(ls[i]))}
for p in g:
    if g[p] == 'O':
        for i in range(p[0]):
            if g[i, p[1]] == '.' and not any(g[k, p[1]] == '#' for k in range(i, p[0])):
                g[i, p[1]] = 'O'
                g[p] = '.'
                break

xr = min(x for x, y in g), max(x for x, y in g)
max_load = xr[1] + 1

print(sum(max_load - x for (x, _), v in g.items() if v == 'O'))
